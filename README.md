# 📚 知识库模板快速开始

欢迎使用终身知识库模板！本指南帮助新用户在 5 分钟内完成环境准备、了解项目结构，并按照“大纲 → 知识点”流程启动个人知识库。

---

## 🎯 模板目标

- 开箱即用的自动化脚本、配置与模板全部集中在 `system/`（system 作为独立仓库）
- 通过 `outlines/` 管理主题大纲，与 `notes/` 中的知识点一一对应
- 借助 `./system/start.sh`、`./system/end.sh` 与 Git 自动化脚本记录每日进展
- 支持用户在知识库根目录的 `config/` 中覆盖默认配置，无需修改模板源码

---

## 🧭 仓库结构速览

**用户知识库仓库结构（例如 `2025learn/`）：**
```
2025learn/                  # 用户知识库根目录
├── system/                 # 克隆的 system 模板仓库
│   ├── init.sh             # 首次使用时的一键初始化
│   ├── start.sh / end.sh   # 日常开始 / 结束脚本
│   ├── scripts/            # Python 自动化工具
│   ├── config/             # 默认配置（可被用户覆盖）
│   ├── templates/          # Markdown 模板
│   └── docs/               # 文档中心（本页所在地）
├── outlines/               # 个人主题大纲（init.sh 初始化后创建）
├── notes/                  # 知识点笔记（init.sh 初始化后创建）
├── reviewsArchived/        # 复习归档(init.sh 初始化后创建)
├── config/                 # 用户自定义配置（覆盖 system/config）
├── reviewsToday.md         # 自动生成的复习任务清单 (start.sh 生成)
├── start.sh                # 快捷启动脚本（init.sh 自动创建，调用 ./system/start.sh）
├── end.sh                  # 快捷结束脚本（init.sh 自动创建，调用 ./system/end.sh）
└── README.md               # 仓库首页说明
```

**system 模板仓库结构（独立仓库）：**
```
system/
├── init.sh                 # 初始化脚本
├── start.sh / end.sh       # 日常脚本
├── scripts/                # Python 自动化工具
├── config/                 # 默认配置
├── templates/              # Markdown 模板
└── docs/                   # 文档中心
```

---

## ⚡ 五步完成首次配置

1. **创建知识库目录**
   ```bash
   mkdir 2025learn
   cd 2025learn
   ```
   或者使用你喜欢的目录名，例如 `my-knowledge-base`。

2. **克隆 system 模板**
   ```bash
   git clone https://github.com/ASCII-S/OutlinesNotesSYS.git system
   ```
   或者如果 system 仓库地址不同，请使用对应的地址。

3. **运行初始化脚本**
   ```bash
   ./system/init.sh
   ```
   - 自动检测依赖
   - 在知识库根目录创建 `notes/`、`outlines/`、`reviewsArchived/` 等目录
   - 复制默认配置到 `config/kb_config.yaml`
   - 自动创建 `start.sh` 和 `end.sh` 快捷脚本

4. **阅读核心文档**
   - `system/docs/INSTALLATION.md`：环境准备与依赖
   - `system/docs/USER_GUIDE.md`：日常工作流与自动化脚本
   - `system/docs/CUSTOMIZATION.md`：配置项与高级玩法

5. **创建第一个主题**
   - 在 `outlines/` 下新建主题文件，例如 `outlines/AI面试路线.md`
   - 编写大纲，按约定结构整理大纲与知识点链接，例如 `[Transformer注意力机制](../notes/AI面试路线/Transformer注意力机制.md)`
   - 通过`ctrl+鼠标左键`大纲中的知识点链接，可以在ide中快速新建文档
   - 编写知识点笔记
   - 在每日结束时使用`./system/end.sh`，会自动初始化元数据

---

## 🔁 推荐工作流

- **每日开始**：运行 `./start.sh` 生成reviewsToday清单、同步远程
- **学习记录**：依据大纲更新知识点笔记，可使用脚本保持元数据一致
- **每日结束**：运行 `./end.sh` 汇总复习结果并执行 Git 提交
- **周期复盘**：使用图谱与统计脚本了解整体进度（详见用户指南）

> **提示**：`init.sh` 会自动在知识库根目录创建 `start.sh` 和 `end.sh` 快捷脚本，它们会调用 `./system/start.sh` 和 `./system/end.sh`。如果这些脚本已存在，初始化时会跳过创建。

---

## ⚙️ 配置覆盖机制

- 模板默认配置：`system/config/kb_config.yaml`
- 用户覆盖配置：`config/kb_config.yaml`（在知识库根目录）
- 加载策略：先读模板默认值，再应用用户配置覆盖

详细字段说明与示例请查阅 `system/docs/CUSTOMIZATION.md`。

---

## 📚 延伸阅读

- `system/docs/INSTALLATION.md` — 系统要求、依赖与初始化细节
- `system/docs/USER_GUIDE.md` — 大纲与笔记协同、脚本命令、每日节奏
- `system/docs/CUSTOMIZATION.md` — 配置项说明、脚本参数与高级玩法
- `system/docs/DEVELOPMENT.md` — 希望二次开发或贡献代码的必读说明

欢迎将本模板分享给更多同样坚持终身学习的伙伴，并在你的仓库 `README.md` 中记录使用心得！

