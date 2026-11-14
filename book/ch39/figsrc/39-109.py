import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

k = 1.5  # mm par km
ox, oy = 6, 22
X, Y, R = 20 * math.sqrt(3), 20.0, 40.0
fig, ax = canvas(72)
px, py = ox + X * k, oy + Y * k
arrow(ax, (ox - 2, oy), (px + 8, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 2), (ox, oy + 44), 'fixe', lw=0.6)
poly(ax, [(ox, oy), (px, oy), (px, py)], 'sujet', fill=True, lw=1.0)
line(ax, [(ox, oy), (px, py)], 'sujet', lw=1.4)
line(ax, [(px, oy), (px, py)], 'varie', lw=1.4)
line(ax, [(ox, oy), (px, oy)], 'varie', lw=1.4)
ax.add_patch(Arc((ox, oy), 22, 22, theta1=0, theta2=30, ec=COL['varie'], lw=1.1, zorder=3))
disc(ax, px, py, 1.5, 'sujet')
disc(ax, ox, oy, 1.3, 'fixe')
text(ax, ox + 15.5, oy + 3.3, '30°', 'varie', 's')
text(ax, ox + 22, oy + 18, r'$r=40$ km', 'sujet', 's', rot=30)
text(ax, (ox + px) / 2, oy - 4.5, r'$x=20\sqrt{3}\approx 34{,}64$ km', 'varie', 's')
text(ax, px + 2, (oy + py) / 2, r'$y=20$ km', 'varie', 's', ha='left')
text(ax, px + 2.5, py + 3, 'avion', 'sujet', 's', ha='left')
text(ax, 44, 13, r'$(20\sqrt{3})^2+20^2=1\,200+400=1\,600=40^2$', 'resultat', 's')
text(ax, 44, 6.5, 'contrôle : on retrouve le rayon', 'resultat', 's')
save(fig, '39-109')
