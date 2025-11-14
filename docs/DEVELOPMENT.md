# 开发指南

本文面向希望扩展或维护终身知识库模板的开发者，介绍项目结构、开发环境与测试流程。

---

## 1. 项目结构回顾

```
system/
├── config/              # 默认配置
├── docs/                # 文档中心
├── scripts/             # Python 与 Shell 脚本
├── templates/           # Markdown 模板
├── init.sh              # 初始化入口
├── start.sh, end.sh     # 日常工作流脚本
└── requirements.txt     # 依赖清单
```

除 `system/` 外，其余目录（`notes/`、`outlines/` 等）属于用户数据，开发时请避免直接修改。

---

## 2. 开发环境

1. 创建虚拟环境并安装依赖：
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r system/requirements.txt
   ```
2. 如需调试知识图谱或可视化功能，请额外安装 Graphviz、pyvis 等依赖。
3. Shell 脚本默认在 Bash 下运行，建议 macOS / Linux / WSL2 环境。

---

## 3. 运行脚本与命令

- 启动每日流程：`./system/start.sh`
- 结束与归档：`./system/end.sh`
- 单独调用 Python 工具：
  ```bash
  python system/scripts/review_manager.py today
  python system/scripts/knowledge_graph.py --all
  ```
- 查看 shell 辅助脚本帮助信息：
  ```bash
  bash system/scripts/kb.sh help
  ```

测试改动时请在临时笔记目录中操作，避免影响真实数据。

---

## 4. 编码规范

- Python：遵循 PEP 8，尽量使用类型注解；必要时引入 `logging` 输出调试信息。
- Shell：启用 `set -euo pipefail`，所有路径使用相对仓库根目录的写法。
- Markdown：使用二级标题起步，保持标题与文件名一致，适度使用表格/列表增强可读性。
- 字符编码：默认 UTF-8，避免引入非必要的非 ASCII 字符。

---

## 5. 测试策略

当前模板以脚本与手动验证为主，建议在提交前完成：

1. **单元测试（可选）**：若新增 Python 模块，可使用 `pytest` 编写测试并在 `tests/` 目录维护。
2. **集成测试**：
   - 创建临时工作目录
   - 拷贝必要脚本与模板
   - 执行 `./system/init.sh`、`./system/start.sh`、`./system/end.sh`
   - 检查生成文件是否符合预期
3. **静态检查**（可选）：启用 `ruff`、`mypy` 或 `shellcheck` 等工具辅助验证。

---

## 6. 文档与示例

- 更新脚本行为时，请同步修改 `system/docs/USER_GUIDE.md` 与相关章节。
- 新增配置项时，补充 `system/docs/CUSTOMIZATION.md` 中的说明。
- 若改动影响快速开始流程，请同步更新 `system/docs/README.md` 与 `QUICKSTART.md`。
- 可在 `examples/` 目录添加演示数据，帮助新用户理解使用方式。

---

## 7. 发布与版本管理

- 推荐使用 Git tag 标记稳定版本，例如 `v1.0.0`。
- 维护 `CHANGELOG.md`（如适用），记录每次版本变更。
- 若计划发布到 GitHub，请在仓库根目录补充 `LICENSE` 与项目简介。
- 模板默认分支命名为 `template`，若用户仓库以此为子模块，请避免强制推送导致破坏性更新。

---

## 8. 常见开发场景

- **新增脚本**：记得在 `system/scripts/__init__.py` 中导出（如需），并在文档中说明用途。
- **调整目录结构**：必要时提供迁移脚本或手册，帮助用户从旧版本升级。
- **引入新依赖**：评估是否必须，必要时提供纯 Python 备选方案。
- **多语言支持**：如需英文版文档，可在 `system/docs/en/` 下维护翻译版本。

---

如有任何疑问或建议，欢迎通过 Issue 或 PR 与维护团队交流。祝开发顺利！***

