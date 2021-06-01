"""
1. 样本X轴的范围是0至9
2. Y轴是0至1的趋势递增的随机正数
3. 打出第二个直方图，Y轴是0至1的趋势递减的随机负数
4. 第一个直方图柱体用蓝色，第二个直方图柱体用绿色，两个直方图之间应有视觉上的分界线
5. 为第一个直方图柱体的上方用文本标注Y轴的值，文本与主题之间应有适当的间隔
6. 为第二个直方图柱体的下方用文本标注Y轴的值，文本与主题之间应有适当的间隔
7. 隐藏所有的刻度
8. 设置适当的坐标轴数据范围，使得两个直方图能够大体居中显示
"""

import numpy as np
from matplotlib import pyplot as plt

n = 10
X = np.arange(0, n)
Y1 = (X+1)/10 * np.random.uniform(0.5,1,n)
Y2 = (X+1)/10 * np.random.uniform(0.5,1,n) * -1

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.bar(X, Y1, fc='b', ec='white')
plt.bar(X, Y2, fc='g', ec='white')

for x, y1, y2 in zip(X, Y1, Y2):
    plt.text(x, y1+0.02, '%.2f' % y1, ha='center', va='bottom')
    plt.text(x, y2-0.02, '%.2f' % y2, ha='center', va='top')

plt.xticks([])
plt.yticks([])
plt.xlim(-1, n)
plt.ylim(-1.5, 1.5)

plt.show()
