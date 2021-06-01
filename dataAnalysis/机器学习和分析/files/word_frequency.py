import sys
import os
from pandas import Series
import jieba
import wordcloud
import matplotlib.pyplot as plt


font = '/usr/share/fonts/truetype/wqy/wqy-microhei.ttf'
excludes = ['的', '和', '是', '随着', '对于', '对', '等', '能', '都',
            '中', '与', '在', '其', '了', '可以', '进行', '有', '更',
            '需要', '提供', '多', '能力', '通过', '会', '不同', '一个',
            '这个', '我们', '将', '并', '同时', '看', '如果', '但', '到',
            '非常', '如何', '包括', '这', '\n', '\t', ' ']


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print('usage: %s file' % os.path.basename(sys.argv[0]))
        exit(1)

    path = sys.argv[1]
    text = open(path).read()

    # 切分词语
    extracted = jieba.cut(text, cut_all=False)
    words = [word for word in extracted if word not in excludes]

    # 词频统计
    word_counts = Series(words).value_counts()

    # 词频展示
    wc = wordcloud.WordCloud(font_path=font, background_color='white',
                             width=1000, height=860, margin=2,
                             max_words=200,
                             max_font_size=100)
    wc.generate_from_frequencies(word_counts)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
