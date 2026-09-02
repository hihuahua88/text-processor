# import jieba.analyse  # 注意：关键词提取要用 jieba.analyse，不是普通的 jieba

# # 从 segment.py 导入分词函数（复用！不要重复写）
# from segment import segment_text


# def extract_keywords(file_path, top_n=5):
#     """
#     从文本中提取关键词
#     :param file_path: 文本文件路径
#     :param top_n: 返回前N个关键词
#     :return: 关键词列表，每个元素是 (词, 权重)
#     """
#     # 第一步：读取文件内容（用 with open，和 segment.py 一样）
#     with open(file_path,'r',encoding='utf-8') as f:
#         text=f.read()
#     # 提示：with open(file_path, 'r', encoding='utf-8') as f:
#     #       text = f.read()
#     # 你自己写这两行

#     # 第二步：用 jieba.analyse.extract_tags 提取关键词
#     keywords=jieba.analyse.extract_tags(text,top_n,withWeight=True)
#     return keywords

#     # 关键API：jieba.analyse.extract_tags(text, topK=top_n, withWeight=True)
#     # text 是上面读到的字符串
#     # topK 是返回几个关键词
#     # withWeight=True 表示同时返回"这个词有多重要"的分数
#     # 返回格式：[('自然语言', 0.8), ('人工智能', 0.6), ...]

#     # 把结果存到 keywords 变量里，然后 return keywords
#     # 你自己写这两行


# if __name__ == "__main__":
#     file_path = "../data/sample.txt"
#     result=extract_keywords(file_path,4)
#     # 调用 extract_keywords 函数
#     # 把结果打印出来
#     # 提示：for word, weight in result:
#     #           print(f"{word}: {weight:.4f}")
#     for word,weight in result:
#         print(f"{word}: {weight:.4f}")
#     # 你自己写


import jieba.analyse


def extract_keywords(file_path, top_n=5):
    """
    从文本中提取关键词
    :param file_path: 文本文件路径
    :param top_n: 返回前N个关键词
    :return: 关键词列表，每个元素是 (词, 权重)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    keywords = jieba.analyse.extract_tags(text, topK=top_n, withWeight=True)
    return keywords


if __name__ == "__main__":
    file_path = "../data/sample.txt"
    result = extract_keywords(file_path, top_n=4)

    print("关键词提取结果：")
    for word, weight in result:
        print(f"{word}: {weight:.4f}")
