import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(70)
line(ax, [(8, 6), (80, 6)], 'fixe', lw=1.4)
line(ax, [(30, 6), (30, 64)], 'fixe', lw=1.4)
text(ax, 32, 62, 'mur vertical', 'fixe', 's', ha='left')
text(ax, 70, 2.5, 'sol', 'fixe', 's')
ph = math.radians(50); Lc = 46
q = (30 + Lc*math.sin(ph), 6 + Lc*math.cos(ph))
arrow(ax, (30, 6), q, 'varie', lw=1.6)
text(ax, q[0], q[1]+3, 'chemin', 'varie', 's')
ax.add_patch(Arc((30, 6), 24, 24, theta1=40, theta2=90, color=COL['autre'], lw=1))
text(ax, 34, 24, 'φ = 50°', 'autre', 's', ha='left')
ax.add_patch(Arc((30, 6), 40, 40, theta1=0, theta2=40, color=COL['resultat'], lw=1))
text(ax, 54, 11, 'α = 40°', 'resultat', 's', ha='left')
text(ax, 12, 40, 'θ = 90°', 'sujet', 'l')
text(ax, 12, 28, 'α = 90° − φ', 'resultat', 's')
save(fig, '27-117')
