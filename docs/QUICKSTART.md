# ⚡ 5 分钟快速上手

想在最短时间内开始使用终身知识库模板？按照以下步骤操作即可完成基础配置并生成第一份复习清单。

---

## 1. 克隆并进入仓库

```bash
git clone https://github.com/<your-account>/knowledge-base-template.git my-kb
cd my-kb
```

---

## 2. （可选）启用虚拟环境

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
```

---

## 3. 运行初始化脚本

```bash
./system/init.sh
```

完成以下事项：

- 检查 Python / Git
- 安装依赖
- 创建 `notes/`、`outlines/`、`reviewsArchived/`
- 生成用户配置 `config/kb_config.yaml`

---

## 4. 创建你的第一个主题

```bash
mkdir -p outlines notes/我的第一个主题
cp system/templates/note_template.md notes/我的第一个主题/示例知识点.md
```

编辑 `outlines/我的第一个主题.md`，写下知识点清单，并链接到对应的笔记：

```markdown
- [示例知识点](../notes/我的第一个主题/示例知识点.md)
```

---

## 5. 生成reviewsToday清单

```bash
./system/start.sh
```

打开仓库根目录下的 `reviewsToday.md`，即可看到自动生成的任务列表。复习完成后勾选条目，并在一天结束时运行：

```bash
./system/end.sh
```

---

## 下一步

- `system/docs/INSTALLATION.md`：了解更多环境细节
- `system/docs/USER_GUIDE.md`：掌握大纲驱动的日常工作流
- `system/docs/CUSTOMIZATION.md`：根据需求调整配置

祝你学习顺利、持续进步！***

