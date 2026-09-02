import jieba


def segment_text(file_path):
    """
    对文本文件进行中文分词
    :param file_path: 文本文件路径
    :return: 分词后的列表
    """
    # 打开文件并读取内容
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 使用 jieba 进行分词
    words = jieba.lcut(text)
    return words


if __name__ == "__main__":
    # 测试代码：直接运行这个文件时执行
    file_path = "../data/sample.txt"
    result = segment_text(file_path)

    print("分词结果：")
    print(result)
    print(f"\n共分出 {len(result)} 个词")
