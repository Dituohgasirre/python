# 二十一、从wikipedia.org 获取Unix的解释页面，按以下要求写一个脚本
#
# 计算出该页面中出现次数最多的10个英文单词，写成一个脚本

import re
import requests


def count_words(words):
    res = {}
    for word in words:
        res[word] = res.get(word, 0) + 1
    return res


def sort_words(words_count):
    return sorted(words_count.items(), key=lambda x: x[1], reverse=True)


def show(words):
    for word, count in words:
        print('%03d %s' % (count, word))


if __name__ == '__main__':
    n = 10
    url = 'https://en.wikipedia.org/wiki/Unix'
    r = requests.get(url)
    clean_text = re.sub(r'<[a-zA-Z0-9]+(?:\s+[^>]+)?>|</[a-zA-Z0-9]+>', '', r.text)
    words = re.findall('[A-Za-z]+', clean_text)
    words_count = count_words(words)
    sorted_words = sort_words(words_count)
    show(sorted_words[:n])
