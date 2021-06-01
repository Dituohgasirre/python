"""
1. 样本数据是元素值全为一的长度为N的一维阵列
2. 扩展度是0.02，其中最后一个扩展度应较其它元素明显
3. 设置一系列颜色供扇型使用
4. 为每个扇型设置标签
5. 设置图的背景色为深灰色
6. 固定坐标轴的XY比值为1
7. 显示每个扇型所占的百分比，数值保留两位小数
8. 扇型边沿线条颜色设置为白色，线条为虚线
9. 字体颜色为白色，大小为12
"""

import numpy as np
import matplotlib.pyplot as plt

n = 7
Z = np.ones(n)
explode = Z*0.02
explode[-1] *= 3
Z[-1] *= 1.2
Z[3] *= 1.5
colors = list('rybgcmk')
labels = ('Righteous', 'Justice', 'Kindness', 'Patience', 'Meekness', 'Humility', 'Love')

fig = plt.figure(facecolor='#999999')
plt.axes([0.025, 0.025, 0.95, 0.95], aspect=1)
plt.pie(Z, explode=explode, colors=colors, labels=labels, autopct='%.2f%%',
        textprops=dict(color='w', fontsize=12), wedgeprops=dict(ec='w', linestyle='--'))

plt.show()
