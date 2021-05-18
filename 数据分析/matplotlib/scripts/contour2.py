"""
1. 样本的X轴是-3至3范围内的100个值，Y轴也一样
2. 高度参数Z的值是X与Y的平方和的平方根
3. 在一张图中打出三个图形
    第一个图形：
        1. 绘制等高填充图形，自动选择4个高度，指定颜色为 [红，黄，蓝，绿]
        2. 给等高填充区域制作颜色示意图
    第二个图形：
        1. 绘制等高填充图形，使用mpl.cm.hot作为cmap，不透明度0.7
        2. 给等高填充区域制作颜色示意图
    第三个图形：
        1. 绘制等高线，颜色白，线宽1，实线，制作等高线标签，标签文字白色
        2. 绘制等高填充区域，使用mpl.cm.hot，不透明度0.7，制作颜色示意图
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

xlist = np.linspace(-3, 3, 100)
ylist = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)

fig = plt.figure()

ax1 = fig.add_subplot(131)
cp = ax1.contourf(X, Y, Z, 3, colors=list('rybg'))
plt.colorbar(cp)

ax2 = fig.add_subplot(132)
cp = ax2.contourf(X, Y, Z, 3, cmap=mpl.cm.hot, alpha=0.7)
plt.colorbar(cp)

ax3 = fig.add_subplot(133)
cp = ax3.contour(X, Y, Z, colors='w', linewidths=1, linestyles='-')
plt.clabel(cp, colors='w')
cp = ax3.contourf(X, Y, Z, cmap=mpl.cm.hot, alpha=0.7)
plt.colorbar(cp)

plt.show()
