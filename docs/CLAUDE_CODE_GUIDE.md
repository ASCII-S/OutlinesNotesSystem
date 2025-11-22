# Claude Code 使用指南

本指南将手把手教你如何使用 Claude Code 自动生成面试大纲和知识点文档。

---

## 📋 目录

1. [前置准备](#前置准备)
2. [配置 Claude Code](#配置-claude-code)
3. [在 VS Code 中使用 Claude Code](#在-vs-code-中使用-claude-code)
4. [创建面试大纲](#创建面试大纲)
5. [创建知识点笔记](#创建知识点笔记)
6. [常见问题](#常见问题)

---

## 前置准备

### 1. 确保已完成初始化

运行初始化脚本，确保 CLAUDE.md 规则文件已就位：

```bash
./system/init.sh
```

初始化完成后，你应该看到以下文件：
- `CLAUDE.md` - 项目根目录的全局规则
- `outlines/CLAUDE.md` - 大纲创建规则
- `notes/CLAUDE.md` - 知识点笔记规则

### 2. 安装 VS Code

确保已安装 [Visual Studio Code](https://code.visualstudio.com/)

---


## 安装node.js 环境

Claude Code 需要 Node.js 环境才能运行。

**使用官方仓库安装（推荐）**
```bash
# 添加 NodeSource 仓库
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
# 安装 Node.js
sudo apt-get install -y nodejs
```

**验证安装是否成功**
安装完成后，打开终端，输入以下命令：
```bash 
node --version
npm --version
```
如果显示版本号，说明安装成功了！


## 配置 Claude Code

### 方法一：使用 npx zcf 快速配置（推荐）

1. **打开终端**，进入项目根目录：

```bash
cd /path/to/your/project
```

2. **运行配置命令**：

```bash
npx zcf
```

3. **按照提示完成配置**：

- 输入1并使用回车以：使用完整初始化
   - 通过回车使用默认配置
   - 不要登录claude code账号，使用`自定义 API 配置`
      - 输入对应的url以及api key

4. **验证配置**：

配置完成后，会在你的用户目录下生成配置文件：
- Linux/macOS: `~/.claude/config.json`

### 方法二：手动配置环境变量
为了让 Claude Code 连接到你的中转服务，需要设置两个环境变量：

#### 临时设置（当前会话）
在终端中运行以下命令：

```bash
export ANTHROPIC_BASE_URL="http://150.158.171.14:9000/api"
export ANTHROPIC_AUTH_TOKEN="你的API密钥" # 一些中转服务使用的可能是ANTHROPIC_API_KEY
```

#### 永久设置
编辑你的 shell 配置文件：

```bash
# 对于 bash (默认)
echo 'export ANTHROPIC_BASE_URL="http://150.158.171.14:9000/api"' >> ~/.bashrc
echo 'export ANTHROPIC_AUTH_TOKEN="你的API密钥"' >> ~/.bashrc
source ~/.bashrc
# 对于 zsh
echo 'export ANTHROPIC_BASE_URL="http://150.158.171.14:9000/api"' >> ~/.zshrc
echo 'export ANTHROPIC_AUTH_TOKEN="你的API密钥"' >> ~/.zshrc
source ~/.zshrc
```
---

## 在 VS Code 中使用 Claude Code

Claude Code 提供两种使用方式：**CLI 命令行模式** 和 **扩展界面模式**。

### 方式一：CLI 命令行模式

#### 1. 打开集成终端

在 VS Code 中按 `` Ctrl+` ``（或 `Cmd+` `）打开集成终端

#### 2. 启动 Claude Code CLI

```bash
claude # 进入claude code 交互模式
```

或者使用别名：

```bash
cc
```

#### 3. 基本命令

```bash
# 查看帮助
claude --help

# 查看版本
claude --version

# 启动交互式会话
claude

# 直接执行命令
claude "帮我创建一个操作系统面试大纲"
```

#### 4. 常用快捷键

在 Claude Code CLI 交互模式中：
- `Ctrl+C` - 中断当前操作
- `Ctrl+D` - 退出 Claude Code
- `/help` - 查看可用命令
- `/clear` - 清空对话历史
- `/exit` - 退出

### 方式二：VS Code 扩展界面模式（推荐）

#### 1. 打开 Claude Code 面板

- **方法 1**：点击 VS Code 右上角的 Claude Code 图标
- **方法 2**：按 `Ctrl+Shift+P`（或 `Cmd+Shift+P`），输入 `Claude Code: Open`

#### 2. 界面说明

Claude Code 面板包含以下部分：
- **对话区域**：显示你和 Claude 的对话
- **输入框**：输入你的指令
- **文件引用区**：显示当前对话中引用的文件
- **工具栏**：包含清空对话、设置等按钮

#### 3. 引用文件到对话

有三种方式将文件引用到 Claude Code：

**方法 1：拖拽文件**
- 从 VS Code 资源管理器中拖拽文件到 Claude Code 输入框

**方法 2：使用 @ 符号**
- 在输入框中输入 `@`，会弹出文件选择器
- 输入文件名进行搜索，选择要引用的文件

**方法 3：右键菜单**
- 在资源管理器中右键点击文件
- 选择 `Send to Claude Code`

---

## 创建面试大纲

### 步骤 1：创建空白大纲文件

在 `outlines/` 目录下创建一个新的 Markdown 文件，例如：

```bash
touch outlines/操作系统面试大纲.md
```

或在 VS Code 中：
1. 右键点击 `outlines/` 目录
2. 选择 `New File`
3. 输入文件名：`操作系统面试大纲.md`

### 步骤 2：将文件引用到 Claude Code

1. 打开 Claude Code 面板
2. 将 `outlines/操作系统面试大纲.md` 引用到对话中（使用上述方法之一）
3. 在输入框中输入指令：

```
请帮我按照规则完成该文档
```

### 步骤 3：Claude 自动生成大纲

Claude Code 会：
1. 读取 `outlines/CLAUDE.md` 中的规则
2. 根据规则和你的指令生成结构化的面试大纲
3. 自动写入到 `outlines/操作系统面试大纲.md` 文件中

### 步骤 4：审查和调整

生成后，你可以：
- 审查大纲结构是否合理
- 要求 Claude 调整某些章节
- 添加或删除知识点

示例调整指令：
```
请在"进程管理"章节中增加"进程间通信"的内容
```

---

## 创建知识点笔记

### 步骤 1：从大纲中选择知识点

打开你创建的大纲文件（如 `outlines/操作系统面试大纲.md`），找到你想要深入学习的知识点。

例如，大纲中有一个知识点：
```
### 进程与线程
- 进程和线程的区别
- 线程的实现方式
```

### 步骤 2：创建对应的笔记文件

在 `notes/` 目录下创建对应的子目录和文件：

```bash
mkdir -p notes/操作系统
touch notes/操作系统/进程和线程的区别.md
```

或在 VS Code 中：
1. 在 `notes/` 下创建 `操作系统/` 目录
2. 在该目录下创建 `进程和线程的区别.md` 文件

### 步骤 3：将文件引用到 Claude Code

1. 打开 Claude Code 面板
2. 将 `notes/操作系统/进程和线程的区别.md` 引用到对话中
3. 在输入框中输入指令：

```
请帮我完成这个知识点的笔记，主题是：进程和线程的区别
```

### 步骤 4：Claude 自动生成笔记

Claude Code 会：
1. 读取 `notes/CLAUDE.md` 中的规则
2. 根据规则生成包含以下部分的笔记：
   - 问题标题
   - 面试标准答案（可背诵）
   - 详细讲解
   - 总结
   - 参考文献
3. 自动写入到笔记文件中

### 步骤 5：深化学习

生成后，你可以：
- 要求 Claude 补充某些细节
- 添加代码示例
- 解释某个概念

示例深化指令：
```
请在"详细讲解"部分添加一个 C 语言的线程创建示例
```

---

## 工作流示例

### 完整流程：从大纲到知识点

假设你要准备"深度学习"面试：

#### 1. 创建大纲

```bash
# 创建空白大纲文件
touch outlines/深度学习面试大纲.md
```

在 Claude Code 中：
```
@outlines/深度学习面试大纲.md
请帮我创建一份深度学习面试大纲，包括基础概念、神经网络、优化算法、常见模型等主题
```

#### 2. 批量创建知识点文件

```bash
# 创建知识点目录
mkdir -p notes/深度学习

# 创建多个知识点文件
touch notes/深度学习/反向传播算法.md
touch notes/深度学习/梯度消失和梯度爆炸.md
touch notes/深度学习/Batch_Normalization原理.md
```

#### 3. 逐个完成知识点

在 Claude Code 中，依次引用每个文件并生成内容：

```
@notes/深度学习/反向传播算法.md
请帮我完成这个知识点的笔记
```

```
@notes/深度学习/梯度消失和梯度爆炸.md
请帮我完成这个知识点的笔记
```

#### 4. 使用脚本管理复习

完成笔记后，使用项目提供的脚本进行复习管理：

```bash
# 生成今日复习清单
./start.sh

# 完成复习后同步进度
./end.sh
```

---

## 高级技巧

### 1. 使用上下文引用

在创建知识点时，可以同时引用大纲文件，让 Claude 更好地理解上下文：

```
@outlines/深度学习面试大纲.md
@notes/深度学习/反向传播算法.md
请根据大纲中的"反向传播算法"部分，帮我完成这个知识点的笔记
```

### 2. 批量处理

如果有多个相关的知识点，可以在一次对话中处理：

```
我要创建以下三个知识点的笔记：
@notes/深度学习/SGD优化器.md
@notes/深度学习/Adam优化器.md
@notes/深度学习/学习率调度策略.md

请依次帮我完成这些笔记，它们都属于"优化算法"主题
```

### 3. 迭代优化

生成初稿后，可以继续优化：

```
请在"详细讲解"部分增加一个对比表格，比较 SGD、Momentum、Adam 三种优化器的特点
```

### 4. 使用 Claude Code 的代码执行功能

对于需要代码示例的知识点，可以让 Claude 直接运行代码验证：

```
请在笔记中添加一个 PyTorch 实现的反向传播示例，并运行验证输出
```

---

## 常见问题

### Q1: Claude Code 无法找到 CLAUDE.md 文件？

**解决方法**：
1. 确保已运行 `./system/init.sh` 初始化脚本
2. 检查以下文件是否存在：
   - `CLAUDE.md`（项目根目录）
   - `outlines/CLAUDE.md`
   - `notes/CLAUDE.md`
3. 如果文件不存在，手动复制：
   ```bash
   cp system/rules/global.mdc CLAUDE.md
   cp system/rules/outline.mdc outlines/CLAUDE.md
   cp system/rules/note.mdc notes/CLAUDE.md
   ```

### Q2: 生成的内容不符合预期格式？

**解决方法**：
1. 检查 CLAUDE.md 规则文件是否正确
2. 在指令中明确说明格式要求
3. 示例：
   ```
   请严格按照 notes/CLAUDE.md 中的格式要求生成笔记
   ```

### Q3: 如何让 Claude 参考网络资料？

**解决方法**：
在指令中明确要求：
```
请帮我创建操作系统面试大纲，可以参考网络上的面试题和资料
```

### Q4: 生成的内容太简单或太复杂？

**解决方法**：
在指令中指定详细程度：
```
请创建一份详细的深度学习面试大纲，每个知识点都要包含3-5个具体的面试问题
```

或

```
请创建一份简洁的操作系统面试大纲，只列出核心知识点即可
```

### Q5: 如何处理中文编码问题？

**解决方法**：
项目已配置 UTF-8 编码（见 `CLAUDE.md`），如果仍有问题：
1. 检查 VS Code 的文件编码设置（右下角状态栏）
2. 确保选择 `UTF-8`
3. 在 VS Code 设置中搜索 `files.encoding`，设置为 `utf8`

### Q6: Claude Code 响应很慢？

**解决方法**：
1. 检查网络连接
2. 考虑使用更快的模型（如 `claude-haiku`）
3. 减少单次引用的文件数量
4. 将大任务拆分为多个小任务

### Q7: 如何保存和复用对话历史？

**解决方法**：
Claude Code 会自动保存对话历史，你可以：
1. 在 Claude Code 面板中查看历史对话
2. 使用 `/history` 命令查看历史
3. 导出对话记录（在设置中配置）

---

## 最佳实践

### 1. 先大纲后笔记

始终先创建完整的大纲，再逐个完成知识点笔记。这样可以：
- 保持知识体系的完整性
- 避免遗漏重要知识点
- 更好地规划学习进度

### 2. 使用清晰的文件命名

- 大纲文件：`<主题>面试大纲.md`
- 笔记文件：`<具体知识点>.md`
- 避免使用特殊字符和空格

### 3. 定期审查和更新

- 每周审查一次大纲，补充新的知识点
- 根据面试反馈更新笔记内容
- 使用 `./kb stats` 查看学习统计

### 4. 善用标签和元数据

在笔记的 frontmatter 中添加有意义的标签：
```yaml
tags: [操作系统, 进程管理, 高频考点]
difficulty: hard
```

### 5. 结合复习脚本

- 每天使用 `./start.sh` 生成复习清单
- 完成复习后使用 `./end.sh` 同步进度
- 定期使用 `./kb stats` 查看掌握情况

---

## 相关文档

- [用户指南](USER_GUIDE.md) - 了解整体工作流
- [快速开始](QUICKSTART.md) - 快速上手指南
- [安装指南](INSTALLATION.md) - 详细安装步骤
- [自定义配置](CUSTOMIZATION.md) - 高级配置选项

---

## 获取帮助

如果遇到问题：
1. 查看 [Claude Code 官方文档](https://code.claude.com/docs)
2. 在项目中运行 `./kb help` 查看可用命令
3. 查看 `system/docs/` 目录下的其他文档

---

**祝你学习愉快！📚**
