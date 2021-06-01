"""
1. 样本的X轴是-3至3范围内的100个值，Y轴也一样
2. 高度参数Z的值是X与Y的平方和的平方根
3. 在一张图中打出三个图形
    第一个图形：
        1. 绘制等高线，线条颜色为黑色、风格为虚线、宽度为0.5
        2. 给等高线制作标签，标签文本需完全覆盖下面的线条
    第二个图形：
        2. 绘制等高线，自动选择4个高度，颜色红，实线，宽度1
        3. 给等高线制作标签，标签文本需完全覆盖下面的线条，文本中保留小数点后两位
    第三个图形：
        2. 绘制等高线，指定4个高度，指定4个颜色，点划线，宽度1
        3. 给等高线制作标签，标签文本需完全覆盖下面的线条，文本中保留小数点后两位
"""

import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-3, 3, 100)
ylist = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)

fig = plt.figure()

ax1 = fig.add_subplot(131, aspect=1)
cp = ax1.contour(X, Y, Z, colors='black', linestyles='--', linewidths=0.5)
plt.clabel(cp, inline=True)

ax2 = fig.add_subplot(132, aspect=1)
cp = ax2.contour(X, Y, Z, 4, colors='red', linestyles='-', linewidths=1)
plt.clabel(cp, inline=True, fmt='%.2f')

ax3 = fig.add_subplot(133, aspect=1)
cp = ax3.contour(X, Y, Z, (1, 1.5, 2, 2.5), colors=list('rgby'), linestyles='-.', linewidths=1)
plt.clabel(cp, inline=True, fmt='%.2f')

plt.show()
