# 自定义与高级配置指南

本指南介绍如何覆盖模板默认配置、扩展脚本能力，并保持与上游模板同步。在动手修改前请先阅读 `system/docs/USER_GUIDE.md` 了解基础工作流。

---

## 1. 配置加载顺序

系统加载配置时遵循以下优先级：

1. 模板默认配置：`system/config/kb_config.yaml`
2. 用户自定义配置：`config/kb_config.yaml`

应用时先读取模板配置，再用用户配置覆盖相同键名的值。你可以只在 `config/kb_config.yaml` 中写需要调整的字段，未覆盖的部分会继续使用默认值。

> **建议**：避免直接编辑 `system/config` 下的文件，以便后续从上游同步更新。

---

## 2. 常见配置字段

虽然各脚本配置略有差异，下列字段在多数场景都会用到：

| 字段                             | 作用                      | 示例                        |
| -------------------------------- | ------------------------- | --------------------------- |
| `review.intervals`               | 间隔重复策略，按难度划分  | `easy: [1, 3, 7, 14]`       |
| `review.daily_limit`             | 当日复习条目上限          | `20`                        |
| `metadata.template`              | 默认 frontmatter 字段列表 | `["title", "created", ...]` |
| `auto_link.similarity_threshold` | 关联笔记相似度阈值（0~1） | `0.65`                      |
| `stats.history_days`             | 统计报表的回溯天数        | `30`                        |
| `paths.outlines`                 | 大纲目录相对路径          | `"outlines"`                |
| `paths.notes`                    | 笔记目录相对路径          | `"notes"`                   |

请查看 `system/config/kb_config.yaml` 了解完整配置项与注释。

---

## 3. 添加自定义脚本

若需新增自动化流程：

1. 在 `system/scripts/` 中创建 Python 脚本，使用现有工具作为参考。
2. 将脚本入口函数加入 `if __name__ == "__main__":` 块，便于命令行执行。
3. 更新 `system/docs/USER_GUIDE.md` 或 `README.md`，说明新增脚本的用途与参数。
4. 如涉及第三方依赖，请在 `system/requirements.txt` 中补充，并测试 `system/init.sh` 能正确安装。

> 可选：为脚本编写单元测试，并在 `system/.github/workflows/` 中配置 CI 验证。

---

## 4. 覆盖 Shell 脚本行为

`system/start.sh`、`system/end.sh` 负责组织每日流程。若你需要对其做出差异化调整，推荐以下做法：

- 复制原脚本至 `custom/` 目录，并在自定义脚本头部引入模板脚本中的函数。
- 或者在用户仓库根目录创建新的 `start.sh`，在其中调用模板脚本并追加自定义步骤：
  ```bash
  #!/bin/bash
  ./system/start.sh
  python custom/send_slack_reminder.py
  ```
- 每次同步上游模板时比对差异，确保自定义脚本保持兼容。

---

## 5. 扩展配置示例

### 5.1 按标签过滤复习清单

在 `config/kb_config.yaml` 中添加：

```yaml
review:
  include_tags: ["核心", "需复习"]
  exclude_tags: ["完成", "归档"]
```

脚本将只挑选包含 `include_tags` 且不包含 `exclude_tags` 的笔记。

### 5.2 自定义大纲与笔记根目录

```yaml
paths:
  outlines: "my_outlines"
  notes: "my_notes"
```

> 修改目录结构后，请同时移动现有文件夹并更新 Git 跟踪。

### 5.3 调整知识图谱输出位置

```yaml
knowledge_graph:
  output_html: "docs/graph/index.html"
  output_markdown: "outlines/_知识图谱.md"
```

---

## 6. 保持模板可升级

- 避免直接修改 `system/` 内的模板文件；如必须修改，请通过 Git 分支或补丁方式管理。
- 当上游模板有更新时，使用以下流程同步：
  ```bash
  git fetch upstream
  git checkout template
  git merge upstream/template
  ```
- 若出现冲突，请优先保留用户配置 (`config/`) 与内容目录 (`outlines/`, `notes/`) 中的更改。

---

## 7. 发布个人定制版本

如果你对模板进行了大量自定义，建议：

1. 在个人仓库的 `README.md` 中记录改动与使用方式。
2. 为新增脚本补充示例与测试数据。
3. 若计划开源，请创建 `CONTRIBUTING.md` 与 `CODE_OF_CONDUCT.md` 说明协作方式。

---

通过灵活配置与扩展脚本，你可以将模板适配到不同的学习场景。若有新的技巧或改进，欢迎通过 Pull Request 或 Issue 分享给社区！***

