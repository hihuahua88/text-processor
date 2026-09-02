# 学习日志

## Day 1 (2026-09-02)
- 创建了 GitHub 仓库并 clone 到本地
- 配置了项目结构（README + log + data + src）
- 安装了 Jieba 分词库，配置了国内镜像源
- 实现了 `segment.py`：读取 txt 文件并进行中文分词
- 实现了 `word_freq.py`：词频统计 + 停用词过滤
- 实现了 `keywords.py`：基于 TF-IDF 的关键词提取
- 学会了 `with open` 读取文件、`jieba.lcut` 分词、`Counter` 计数
- 学会了看 VS Code 悬浮提示框来调用陌生 API
- 卡住：一开始文件名打错（word_freg 而不是 word_freq），已解决
- 明天目标：文本相似度计算（Jaccard + 余弦相似度）
