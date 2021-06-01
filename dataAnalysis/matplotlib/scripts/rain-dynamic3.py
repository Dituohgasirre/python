import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def updater(frame, params):
    P = params['P']
    S = params['S']
    C = params['C']
    points = params['points']
    sizemin = params['sizemin']
    sizemax = params['sizemax']
    n = len(P)

    # all points get larger
    S += (sizemax - sizemin) / 30

    # all points' edgecolor get lighter (closer to transparent)
    delta = 0.02
    C[:,-1] = np.maximum(0, C[:,-1] - delta)

    # reset one point
    i = frame % n
    P[i] = np.random.uniform(0,1,2)
    S[i] = sizemin
    C[i,-1] = 1     # opaque level
    # set color for the ring
    # C[i,:3] = np.random.uniform(0,1,3)

    points.set_offsets(P)
    points.set_sizes(S)
    points.set_edgecolors(C)


# number of rings
n = 70
sizemin = 50
sizemax = 50*50

# no toolbar
mpl.rcParams['toolbar'] = 'None'

# random positions
P = np.random.uniform(0,1,(n,2))

# sizes, different sizes initially
S = np.linspace(sizemin, sizemax, n)

# edge colors
# transparent(0) -> opaque(1)
C = np.zeros((n, 4))
C[:,-1] = np.linspace(1,0,n)

# fig, axes
fig = plt.figure(figsize=(6,6), facecolor='white')
ax = fig.add_subplot(1, 1, 1, aspect='equal')

# figure settings, tight layout
fig.set_tight_layout(True)

# axes settings, no spines, no ticks, set limits
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

scat = ax.scatter(P[:,0], P[:,1], s=S, edgecolor=C, facecolor='None',
        linewidth=1.5)
params = dict(P=P, S=S, C=C, points=scat, sizemin=sizemin, sizemax=sizemax)
animation = FuncAnimation(fig, updater, interval=20, frames=1000, fargs=(params,))

plt.show()
