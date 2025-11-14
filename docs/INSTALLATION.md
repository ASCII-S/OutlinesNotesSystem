# 安装与初始化指南

本指南帮助你在全新环境中部署终身知识库模板，准备好运行自动化脚本与 Git 工作流。

---

## 1. 系统要求

- 操作系统：macOS、Linux 或 WSL2（建议开启 Git、Python 支持）
- Python：3.9 及以上版本（内置 `venv` 模块）
- Git：2.30 及以上版本
- 可选：Node.js（若后续想扩展前端可视化）、Graphviz（知识图谱渲染）

---

## 2. 克隆模板

```bash
git clone https://github.com/<your-account>/knowledge-base-template.git system
cd system
```

如果你计划长期跟进上游模板更新，建议在仓库中添加 upstream：

```bash
git remote add upstream https://github.com/<template-author>/knowledge-base-template.git
```

---

## 3. 创建虚拟环境（推荐）

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install --upgrade pip
```

---

## 4. 安装依赖

模板会在初始化脚本中自动安装依赖，你也可以手动执行：

```bash
pip install -r system/requirements.txt
```

如需额外依赖（例如 `jieba`、`networkx`、`pyvis`），请在 `system/requirements.txt` 中补充后重新安装。

---

## 5. 运行初始化脚本

```bash
./system/init.sh
```

初始化脚本将完成以下操作：

1. 检查 Python、Git 是否可用
2. 安装 `system/requirements.txt` 中列出的依赖
3. 创建用户目录：`notes/`、`outlines/`、`reviewsArchived/` 等
4. 如不存在用户配置，则复制 `system/config/kb_config.yaml` 至 `config/kb_config.yaml`
5. 提示是否初始化 Git 仓库并拷贝模板 `.gitignore`

> 首次执行后，如果你希望将模板适配为自己的仓库，请更新`config/kb_config.yaml` 中的个性化信息。

---

## 6. 验证安装

执行以下命令确认脚本可运行：

```bash
./system/start.sh         # 生成或更新reviewsToday清单
python system/scripts/review_manager.py --help
```

若命令执行成功，即表示初始化完成。

---

## 7. 常见问题

- **Python 版本不符合**：使用 `pyenv` 或 `conda` 安装合适版本，再创建虚拟环境。
- **pip 安装失败**：检查代理设置或换用国内镜像源，例如 `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r system/requirements.txt`
- **脚本执行权限不足**：为所有 `.sh` 脚本添加可执行权限：
  ```bash
  chmod +x system/*.sh
  chmod +x system/scripts/*.sh 2>/dev/null || true
  ```
- **Git 子模块尚未拉取**：若模板未来引入子模块，请运行 `git submodule update --init --recursive`

---

做好以上准备后，请继续阅读 `system/docs/USER_GUIDE.md`，了解每日工作流与笔记结构。祝学习顺利！***

