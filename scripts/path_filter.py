#!/usr/bin/env python3
"""
路径过滤工具
提供统一的文件/目录忽略逻辑
"""

import re
from pathlib import Path
from typing import List, Set, Callable, Dict
import fnmatch


class PathFilter:
    """路径过滤器，用于统一的忽略规则管理"""

    def __init__(self, config: dict, base_dir: Path):
        """
        初始化路径过滤器

        Args:
            config: scan_ignore配置块
            base_dir: 基准目录（通常是notes_dir）
        """
        self.config = config
        self.base_dir = base_dir
        self.enabled = config.get('enabled', True)

        # 缓存git子模块列表
        self._submodules_cache = None

        # 预编译正则表达式
        self._regex_patterns = []
        if 'patterns' in config and config.get('patterns') and 'regex' in config['patterns']:
            regex_patterns = config['patterns'].get('regex') or []
            for pattern in regex_patterns:
                try:
                    self._regex_patterns.append(re.compile(pattern))
                except re.error as e:
                    print(f"⚠️  正则表达式编译失败: {pattern} - {e}")

    def should_ignore(self, path: Path) -> bool:
        """
        判断路径是否应该被忽略

        Args:
            path: 要检查的路径（绝对路径）

        Returns:
            True表示应该忽略，False表示应该处理
        """
        if not self.enabled:
            return False

        try:
            # 获取相对路径（相对于base_dir）
            rel_path = path.relative_to(self.base_dir)
            rel_path_str = str(rel_path)
        except ValueError:
            # 路径不在base_dir下，忽略
            return True

        patterns = self.config.get('patterns') or {}

        # 1. 检查精确路径匹配
        exact_paths = patterns.get('exact_paths') or []
        for exact_path in exact_paths:
            # 支持目录和文件的精确匹配
            if rel_path_str == exact_path or rel_path_str.startswith(exact_path + '/'):
                return True

        # 2. 检查通配符模式
        globs = patterns.get('globs') or []
        for glob_pattern in globs:
            if fnmatch.fnmatch(rel_path_str, glob_pattern):
                return True
            # 同时检查父目录匹配
            if fnmatch.fnmatch(str(path.parent.relative_to(self.base_dir)), glob_pattern):
                return True

        # 3. 检查正则表达式
        for regex_pattern in self._regex_patterns:
            if regex_pattern.search(rel_path_str):
                return True

        # 4. 检查文件名/目录名
        ignore_names = self.config.get('ignore_names', [])
        if path.name in ignore_names:
            return True

        # 检查路径中的任何部分是否在忽略名单中
        for part in path.parts:
            if part in ignore_names:
                return True

        # 5. 检查前缀
        ignore_prefixes = self.config.get('ignore_prefixes', ['.'])
        for prefix in ignore_prefixes:
            if path.name.startswith(prefix):
                return True

        # 6. 检查是否为git子模块
        if self.config.get('auto_detect_submodules', True):
            if self._is_git_submodule(path):
                return True

        return False

    def _is_git_submodule(self, path: Path) -> bool:
        """检查路径是否在git子模块内"""
        if self._submodules_cache is None:
            self._submodules_cache = self._detect_git_submodules()

        try:
            rel_path = path.relative_to(self.base_dir)
            # 检查路径是否在任何子模块内
            for submodule in self._submodules_cache:
                if rel_path == submodule:
                    return True
                try:
                    # 检查路径是否在子模块目录下
                    rel_path.relative_to(submodule)
                    return True
                except ValueError:
                    continue
            return False
        except ValueError:
            return False

    def _detect_git_submodules(self) -> Set[Path]:
        """检测所有git子模块（相对路径）"""
        submodules = set()

        try:
            # 查找所有包含.git文件（而非目录）的路径
            for git_file in self.base_dir.rglob(".git"):
                if git_file.is_file():  # .git是文件说明是子模块
                    submodule_dir = git_file.parent
                    try:
                        rel_path = submodule_dir.relative_to(self.base_dir)
                        submodules.add(rel_path)
                    except ValueError:
                        continue
        except Exception as e:
            print(f"⚠️  Git子模块检测失败: {e}")

        return submodules

    def filter_paths(self, paths: List[Path]) -> List[Path]:
        """批量过滤路径列表"""
        return [p for p in paths if not self.should_ignore(p)]

    def create_file_filter(self) -> Callable[[Path], bool]:
        """创建文件过滤函数（用于rglob等场景）"""
        def file_filter(path: Path) -> bool:
            return not self.should_ignore(path)
        return file_filter


def create_path_filter(config: dict, notes_dir: Path = None) -> PathFilter:
    """
    创建路径过滤器的便捷函数

    Args:
        config: 完整的kb_config配置
        notes_dir: notes目录路径（可选，如果不提供则从config中获取）

    Returns:
        PathFilter实例
    """
    # 获取notes目录
    if notes_dir is None:
        ROOT_DIR = Path(__file__).parent.parent.parent
        notes_dir = ROOT_DIR / config['paths'].get('notes_dir', 'notes')

    # 获取scan_ignore配置
    scan_ignore = config.get('scan_ignore', {
        'enabled': True,
        'patterns': {},
        'ignore_prefixes': ['.'],
        'auto_detect_submodules': True
    })

    return PathFilter(scan_ignore, notes_dir)


if __name__ == '__main__':
    """测试路径过滤器"""
    import yaml

    # 加载配置
    config_file = Path(__file__).parent.parent / 'config' / 'kb_config.yaml'
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # 创建过滤器
    path_filter = create_path_filter(config)

    # 测试路径
    ROOT_DIR = Path(__file__).parent.parent.parent
    notes_dir = ROOT_DIR / 'notes'

    test_paths = [
        notes_dir / '精通vllm源码' / 'vllm' / 'README.md',
        notes_dir / '精通vllm源码' / '正常笔记.md',
        notes_dir / '.hidden' / 'file.md',
        notes_dir / '_seeds' / 'test.md',
    ]

    print("🧪 路径过滤器测试：")
    for test_path in test_paths:
        should_ignore = path_filter.should_ignore(test_path)
        status = "❌ 忽略" if should_ignore else "✅ 处理"
        print(f"  {status}: {test_path.relative_to(ROOT_DIR)}")

    # 显示检测到的子模块
    if path_filter._submodules_cache:
        print(f"\n📦 检测到 {len(path_filter._submodules_cache)} 个Git子模块：")
        for sm in path_filter._submodules_cache:
            print(f"  - {sm}")
