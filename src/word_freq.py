from segment import segment_text
from collections import Counter


def word_frequency(words, top_n=10):
    """
    统计词频并过滤停用词
    :param words: 分词后的列表
    :param top_n: 返回前N个高频词
    :return: 按频率排序的列表，元素为 (词, 次数)
    """
    # 停用词：无实际意义的虚词、代词等
    # 用集合（set）存储，因为 "in" 判断在集合里非常快
    stop_words = {
        '的',
        '了',
        '是',
        '我',
        '你',
        '它',
        '在',
        '和',
        '一个',
        '为',
        '让',
        '如何',
        '并',
        '与',
        '对',
        '及',
        '等',
    }

    # 过滤：只保留"有意义的词"
    filtered = []
    for word in words:
        # 条件1：不在停用词列表里
        # 条件2：长度大于1（过滤单字，如"我"、"它"）
        # 条件3：是字母/数字/中文（过滤标点符号，如"。"、"，"）
        if word not in stop_words and len(word) > 1 and word.isalnum():
            filtered.append(word)

    # Counter 是 Python 内置的计数器，自动统计每个元素出现几次
    counter = Counter(filtered)

    # most_common(n) 返回出现次数最多的前 n 个
    # 结果格式：[('自然语言', 2), ('人工智能', 1), ...]
    return counter.most_common(top_n)


if __name__ == "__main__":
    file_path = "../data/sample.txt"

    # 第一步：分词（直接调用 segment.py 里的函数，不用重复写）
    words = segment_text(file_path)
    print("分词结果：")
    print(words)

    # 第二步：词频统计
    print("\n词频统计（前10个）：")
    freq = word_frequency(words, top_n=10)

    # freq 里的每个元素是 (词, 次数) 的元组
    for word, count in freq:
        print(f"{word}: {count}次")
