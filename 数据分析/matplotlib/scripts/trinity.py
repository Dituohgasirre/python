import numpy as np
import matplotlib.pyplot as plt

line_color = 'blue'
line_size = 20
point_color = 'red'
point_size = 3000
radius = 1
font_size = 20

# define points
up = [0, radius]
left = [np.cos(np.pi*210/180)*radius, np.sin(np.pi*210/180)*radius]
right = [np.cos(np.pi*-30/180)*radius, np.sin(np.pi*-30/180)*radius]
points = np.array([up, left, right])

# plot points and lines, set points over lines
plt.plot(points[:2,0], points[:2,1], color=line_color, linewidth=line_size)
plt.plot(points[-2:,0], points[-2:,1], color=line_color, linewidth=line_size)
plt.plot(points[[0,2],0], points[[0,2],1], color=line_color, linewidth=line_size)
dots = plt.scatter(points[:,0], points[:,1], point_size, color=point_color)
dots.zorder = 100

ax = plt.gca()
# hide the spines
for spine in ax.spines.values():
    spine.set_visible(False)

# remove ticks
plt.xticks([])
plt.yticks([])

# set aspect ratio
ax.set_aspect('equal')

# set texts
plt.annotate('God', xy=(0,0), xycoords='data', xytext=(-10,0),
        textcoords="offset points", fontsize=font_size)
plt.annotate('Father', xy=up, xycoords='data', xytext=(-30, 40), textcoords="offset points", fontsize=font_size)
plt.annotate('HolyGhost', xy=left, xycoords='data', xytext=(-50, -50), textcoords="offset points", fontsize=font_size)
plt.annotate('Son', xy=right, xycoords='data', xytext=(-15, -50), textcoords="offset points", fontsize=font_size)

plt.show()
