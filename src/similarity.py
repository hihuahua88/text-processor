import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cos_sim
from segment import segment_text


def jaccard_similarity(words1, words2):
    """
    计算Jaccard相似度
    :param words1: 文本1的分词列表
    :param words2: 文本2的分词列表
    :return: 相似度分数（0.0-1.0之间）
    """
    # 第一步：把列表转成集合（set会自动去重）
    # 提示：set1 = set(words1)
    #       set2 = set(words2)
    # 你自己写这两行
    set1 = set(words1)
    set2 = set(words2)

    # 第二步：求交集（两个文本都出现的词）
    # 提示：intersection = set1 & set2
    # 你自己写这一行
    intersection = set1 & set2

    # 第三步：求并集（两个文本出现过的所有词，不重复）
    # 提示：union = set1 | set2
    # 你自己写这一行
    union = set1 | set2

    # 第四步：防止除以0（如果两段文本都是空的）
    # 提示：if len(union) == 0:
    #           return 0.0
    # 你自己写这两行
    if len(union) == 0:
        return 0.0

    # 第五步：Jaccard公式 = 交集大小 ÷ 并集大小
    # 提示：return len(intersection) / len(union)
    # 你自己写这一行
    return len(intersection) / len(union)


def cosine_similarity(text1, text2):
    """
    计算余弦相似度
    :param text1: 文本1的原始字符串
    :param text2: 文本2的原始字符串
    :return: 相似度分数（0.0-1.0之间）
    """
    # TfidfVectorizer 默认按"空格"分词，适合英文
    # 中文需要先分词，再用空格把词连起来
    words1 = jieba.lcut(text1)
    words2 = jieba.lcut(text2)

    # 用空格把词列表连成字符串
    # 提示：doc1 = " ".join(words1)
    #       doc2 = " ".join(words2)
    # 你自己写这两行
    doc1 = " ".join(words1)
    doc2 = " ".join(words2)

    # 把两段文本转成 TF-IDF 向量
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([doc1, doc2])

    # 计算两个向量的余弦相似度
    # tfidf_matrix[0:1] 是第1段文本的向量
    # tfidf_matrix[1:2] 是第2段文本的向量
    # 提示：similarity = cos_sim(tfidf_matrix[0:1], tfidf_matrix[1:2])
    # 你自己写这一行
    similarity = cos_sim(tfidf_matrix[0:1], tfidf_matrix[1:2])

    # 返回结果（从二维数组里取出那个数字）
    return float(similarity[0][0])


if __name__ == "__main__":
    file1 = "../data/sample.txt"
    file2 = "../data/sample2.txt"

    # 读取原始文本
    # 提示：用 with open(file1, 'r', encoding='utf-8') as f:
    #           text1 = f.read()
    # 同样方式读 file2 到 text2
    # 你自己写这四行
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()

    # Jaccard相似度（基于分词后的集合）
    # 提示：words1 = segment_text(file1)
    #       words2 = segment_text(file2)
    #       jaccard = jaccard_similarity(words1, words2)
    # 你自己写这三行
    words1 = segment_text(file1)
    words2 = segment_text(file2)
    jaccard = jaccard_similarity(words1, words2)
    print(f"Jaccard相似度: {jaccard:.4f}")

    # 余弦相似度（基于TF-IDF向量）
    # 提示：cosine = cosine_similarity(text1, text2)
    # 你自己写这一行
    cosine = cosine_similarity(text1, text2)

    print(f"余弦相似度: {cosine:.4f}")
