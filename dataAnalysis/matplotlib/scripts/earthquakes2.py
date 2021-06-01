import urllib
import numpy as np
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from  matplotlib.animation import FuncAnimation


def update(frame):
    eq_idx = frame % len(EQ)
    point_idx = frame % len(P)

    #
    # update color and size
    #
    P['color'][:,3] = np.maximum(0, P['color'][:,3] - 1.0/len(P))
    P['size'] += P['growth']

    #
    # reset one point
    #
    magnitude = EQ['magnitude'][eq_idx]
    position = EQ['position'][eq_idx]
    P['position'][point_idx] = map(*position)
    P['size'][point_idx] = 5    # initial size
    # growing speed depends on magnitude
    P['growth'][point_idx]= np.exp(magnitude) * 0.1

    if magnitude < 6:
        P['color'][point_idx]    = 0,0,1,1  # blue for magnitude less than 6
    else:
        P['color'][point_idx]    = 1,0,0,1  # red otherwise

    #
    # apply changes
    #
    # face color is lighter than the edge color
    scat.set_edgecolors(P['color'])
    scat.set_facecolors(P['color']*(1,1,1,0.25))
    scat.set_sizes(P['size'])
    scat.set_offsets(P['position'])


# prepare earthquake data
data_fname = '4.5_month.csv'
lines = open(data_fname).read().splitlines()[1:-1]
EQ = np.zeros(len(lines), dtype=[('position',  float, 2),
                                 ('magnitude', float, 1)])
for i,line in enumerate(lines):
    row = line.split(',')
    EQ['position'][i] = float(row[2]), float(row[1])
    EQ['magnitude'][i] = float(row[4])

# prepare point data
P = np.zeros(50, dtype=[('position', float, 2),
                        ('size',     float, 1),
                        ('growth',   float, 1),
                        ('color',    float, 4)])

fig = plt.figure(figsize=(14,10))
ax = plt.subplot(1,1,1)

# Basemap projection
map = Basemap(projection='mill')
map.drawcoastlines(color='0.50', linewidth=0.25)
map.fillcontinents(color='0.95')
scat = ax.scatter(P['position'][:,0], P['position'][:,1], P['size'], lw=0.5,
                  edgecolors = P['color'], facecolors='None', zorder=10)

plt.title("Earthquakes > 4.5 in the last 30 days")
animation = FuncAnimation(fig, update, interval=10)
plt.show()
