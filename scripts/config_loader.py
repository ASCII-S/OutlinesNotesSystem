#!/usr/bin/env python3
"""
配置加载工具
实现配置合并覆盖机制：
1. 先加载系统默认配置 (system/config/kb_config.yaml)
2. 再加载用户配置 (config/kb_config.yaml)，覆盖相同键名的值
3. 支持深层字典合并
"""

import yaml
from pathlib import Path
from typing import Dict, Any


def deep_merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """
    深度合并两个字典，override 中的值会覆盖 base 中的值
    对于嵌套字典，会递归合并而不是完全替换
    """
    result = base.copy()
    
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # 递归合并嵌套字典
            result[key] = deep_merge(result[key], value)
        else:
            # 直接覆盖
            result[key] = value
    
    return result


def load_config(root_dir: Path = None) -> Dict[str, Any]:
    """
    加载配置文件，实现合并覆盖机制
    
    Args:
        root_dir: 项目根目录路径，如果为 None 则自动检测（从脚本位置向上查找）
    
    Returns:
        合并后的配置字典
    """
    if root_dir is None:
        # 自动检测根目录（脚本在 system/scripts/ 中，向上两级到根目录）
        root_dir = Path(__file__).parent.parent.parent
    
    template_config_path = root_dir / "system" / "config" / "kb_config.yaml"
    user_config_path = root_dir / "config" / "kb_config.yaml"
    
    # 1. 加载系统默认配置
    base_config = {}
    if template_config_path.exists():
        try:
            with open(template_config_path, 'r', encoding='utf-8') as f:
                base_config = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"警告: 无法加载系统默认配置 {template_config_path}: {e}")
            base_config = {}
    else:
        print(f"警告: 系统默认配置文件不存在: {template_config_path}")
    
    # 2. 加载用户配置（如果存在）
    user_config = {}
    if user_config_path.exists():
        try:
            with open(user_config_path, 'r', encoding='utf-8') as f:
                user_config = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"警告: 无法加载用户配置 {user_config_path}: {e}")
            user_config = {}
    
    # 3. 合并配置（用户配置覆盖系统默认配置）
    if user_config:
        merged_config = deep_merge(base_config, user_config)
    else:
        merged_config = base_config
    
    return merged_config


if __name__ == "__main__":
    # 测试配置加载
    config = load_config()
    import json
    print(json.dumps(config, indent=2, ensure_ascii=False))

