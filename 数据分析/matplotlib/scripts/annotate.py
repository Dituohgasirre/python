"""
1. 使图像更宽 (figsize)
2. 使曲线更粗 (linewidth)
3. 给线条设置标签 (label)
4. 使X，Y轴与数据曲线之间留出一些空位 (X.min, X.max)
5. X轴刻度及标签：-π, -π/2, 0, +π/2, +π
    π 的latex表示法: r'$\pi$'
6. Y轴刻度及标签：-1, 0, +1
7. 隐藏上边和右边的轴线
8. 把左边和下边的轴线移动到数据空间的(0,0)点
9. 把图例说明打在图像的左上方，不显示边框
10. 在两条曲线上打出X值为2π/3的点，颜色与所在的曲线相同
11. 在两个点之间画虚线，X轴上段的颜色与上方曲线相同，下段曲线颜色与下方曲线相同
12. 给两个点打出注解文字
    1. 正弦文本的Python代码(Latex)：r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$'
    2. 正弦文本位于点的右上方 (textcoords="offset points")
    3. 余弦文本的Python代码(Latex)：r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$'
    4. 余弦文本位于点的左下方 (textcoords="offset points")
    5. 箭头属性：dict(arrowstyle="->", connectionstyle="arc3,rad=.2")
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
S = np.sin(X)

fig = plt.figure(figsize=(10, 6), dpi=80)
plt.plot(X, S, color='blue', linewidth=2.5, linestyle='-', label='sine')
plt.plot(X, C, color='red', linewidth=2.5, linestyle='-', label='cosine')
plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='upper left', frameon=False)

t = 2*np.pi/3
sint = np.sin(t)
cost = np.cos(t)
plt.scatter([t], [sint], 50, color='blue')
plt.scatter([t], [cost], 50, color='red')
plt.plot([t,t], [0, sint], color='blue', linewidth=1.5, linestyle='--')
plt.plot([t,t], [0, cost], color='red', linewidth=1.5, linestyle='--')
formula_sin = r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$'
formula_cos = r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$'
plt.annotate(formula_sin, xy=(t, sint), xycoords='data',
             xytext=(10, 50), textcoords="offset points",
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
plt.annotate(formula_cos, xy=(t, cost), xycoords='data',
             xytext=(-90, -50), textcoords="offset points",
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

labels = ax.get_xticklabels() + ax.get_yticklabels()
for label in labels:
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='None'))
for line in ax.lines:
    line.zorder = -1

plt.show()
