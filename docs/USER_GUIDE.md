# 使用指南：大纲驱动的终身知识库

本指南帮助你理解知识库模板的日常工作流，从创建大纲到维护知识点，以及如何运用自动化脚本保持高效。

---

## 1. 工作流概览

1. **规划主题**：在 `outlines/` 中创建主题大纲，拆分知识点与复习节奏。
2. **撰写知识点**：在 `notes/<主题>/` 内撰写 Markdown 笔记，保持 frontmatter 元数据完整。
3. **自动化支持**：使用 `system/scripts/` 提供的工具生成复习清单、统计报表、知识图谱等。
4. **每日自检**：通过 `system/start.sh`、`system/end.sh` 形成稳定的学习与复盘节奏。

---

## 2. 目录与命名约定

- `outlines/`: 每个主题一个 Markdown 文件，文件名建议使用中文/英文描述主题，例如 `outlines/深度学习工程师.md`。
- `notes/<主题>/`: 与大纲对应的知识点目录，笔记文件建议与大纲条目一致，例如 `notes/深度学习工程师/Transformer注意力机制.md`。
- `reviewsToday.md`: 自动生成的复习任务清单，请勿手动删除；每日结束时由脚本归档。
- `reviewsArchived/`: 自动创建的历史复习记录。

确保大纲中的链接指向对应的 `notes/` 文件，以便实现「大纲 → 知识点」映射。

---

## 3. Frontmatter 模板

使用 `system/templates/note_template.md` 作为新笔记的起点，推荐保留以下字段：

```yaml
---
title: Transformer注意力机制
created: 2025-01-01
last_reviewed: 2025-01-01
next_review: 2025-01-02
review_count: 0
difficulty: medium
mastery_level: 0.0
tags: [深度学习, transformer]
related_outlines:
  - outlines/深度学习工程师.md
---
```

> `last_reviewed`、`next_review`、`review_count`、`mastery_level` 会由脚本自动更新，手动调整 `difficulty` 与 `tags` 有助于更精准的复习安排。

---

## 4. 每日脚本工作流

### 4.1 开始一天：`system/start.sh`

主要步骤：

1. 从远程仓库拉取最新模板更新（可选）
2. 生成或更新 `reviewsToday.md`
3. 提示当天需要关注的大纲与知识点

使用方式：

```bash
./system/start.sh
```

### 4.2 结束一天：`system/end.sh`

主要步骤：

1. 根据 `reviewsToday.md` 中已完成的项目同步笔记元数据
2. 将当日复习清单归档至 `reviewsArchived/`
3. 整理 Git 提交（可选自动提交）

使用方式：

```bash
./system/end.sh
```

---

## 5. 核心 Python 脚本

所有脚本位于 `system/scripts/`，均可通过 `python system/scripts/<script>.py --help` 查看详细参数。

| 脚本                 | 功能                                    | 常用命令                                         |
| -------------------- | --------------------------------------- | ------------------------------------------------ |
| `review_manager.py`  | 生成复习清单、标记复习完成、调整难度    | `python system/scripts/review_manager.py today`  |
| `add_metadata.py`    | 为缺少 frontmatter 的笔记补全基础元数据 | `python system/scripts/add_metadata.py`          |
| `auto_link.py`       | 自动插入相关笔记与跨主题索引            | `python system/scripts/auto_link.py update-all`  |
| `knowledge_graph.py` | 生成知识图谱（HTML/Markdown）           | `python system/scripts/knowledge_graph.py --all` |
| `stats_generator.py` | 输出学习统计报表                        | `python system/scripts/stats_generator.py`       |

> 若你习惯使用快捷命令，可在仓库根目录封装自定义 `Makefile` 或 shell 脚本。

---

## 6. 主题与笔记关联实践

1. **在大纲中引用笔记**  
   使用 Markdown 链接，将大纲条目指向 `notes/`：
   ```markdown
   - [Transformer注意力机制](../notes/深度学习工程师/Transformer注意力机制.md)
   ```
2. **在笔记中回链大纲**  
   在笔记的 `related_outlines` 中记录关联大纲路径，脚本会使用这些信息生成复盘报告。
3. **批量处理**  
   使用 `auto_link.py` 扫描并补全相关笔记区块，帮助发现跨主题关联。

---

## 7. Git 与版本管理建议

- 每次运行 `system/end.sh` 后检查变更，再执行 `git status` 与 `git diff` 确认内容。
- 建议以「主题」为粒度提交，例如 `git commit -m "Add Transformer attention note"`。
- 定期与模板上游同步：
  ```bash
  git fetch upstream
  git merge upstream/template
  ```
- 若使用 GitHub Actions/CI，请在 `system/` 中维护相关工作流配置。

---

## 8. 常见问题

- **复习清单为空**：确认大纲中是否链接了笔记，或检查 `config/kb_config.yaml` 中的复习间隔设置。
- **脚本找不到文件**：请确保大纲引用路径与笔记目录结构一致，注意大小写与空格。
- **统计报表缺少字段**：检查笔记 frontmatter 是否包含 `review_count`、`mastery_level` 等字段。
- **想暂停某些主题**：可在大纲中暂时移除链接，或在笔记 frontmatter 中标记 `difficulty: easy` 以降低复习频率。

---

熟悉上述工作流后，你已经掌握了模板的核心使用方式。下一步可阅读 `system/docs/CUSTOMIZATION.md`，根据需求调整配置与脚本行为。祝学习顺利！***

