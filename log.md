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


## Day 2 (2026-09-03)
- 实现了 `similarity.py`：Jaccard 相似度 + 余弦相似度计算
- 学会了集合的交集（`&`）和并集（`|`）运算
- 理解了 `TfidfVectorizer` 把文本转成向量的过程
- 理解了稀疏矩阵和 `fit_transform` 的作用
- 学会了 `[0:1]` 切片保持二维矩阵形状
- 项目四个核心功能全部完成：分词 → 词频 → 关键词 → 相似度
- 卡住：一开始不理解 `join` 和矩阵切片，已解决
- 下一步：整合所有功能到一个入口文件，或增加更多测试文本