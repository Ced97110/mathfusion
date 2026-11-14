import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(64)
cx, cy, u = 14, 10, 10
for i in range(0, 6):
    for j in range(0, 5):
        disc(ax, cx + i*u*0.9, cy + j*u*0.9, 0.45, 'fixe')
P = lambda a, b: (cx + a*u*0.9, cy + b*u*0.9)
line(ax, [P(0, 0), P(4.4, 4.4)], 'fixe', dash=True)
line(ax, [P(0, 0), P(5, 0)], 'fixe'); line(ax, [P(0, 0), P(0, 4.4)], 'fixe')
ax.add_patch(Arc((cx, cy), 18, 18, theta1=0, theta2=45, ec=COL['varie'], lw=1.1, zorder=3))
ax.add_patch(Arc((cx, cy), 30, 30, theta1=0, theta2=90, ec=COL['autre'], lw=1.1, zorder=3))
arrow(ax, P(3, 1), P(1, 3), 'varie', lw=1.2, both=False)
disc(ax, *P(0, 0), 0.9, 'encre')
disc(ax, *P(3, 1), 1.4, 'sujet'); disc(ax, *P(1, 3), 1.4, 'resultat')
text(ax, P(3, 1)[0] + 2.5, P(3, 1)[1] - 2.5, r'$P\ (3\ ;\ 1)$', 'sujet', 's', ha='left')
text(ax, P(1, 3)[0] - 2.5, P(1, 3)[1] + 3, r'$S_\varphi(P)\ (1\ ;\ 3)$', 'resultat', 's', ha='left')
text(ax, 58, 20, r'axe : $\varphi/2=45°$', 'varie', 's', ha='left')
text(ax, 58, 14, r'$\varphi=90°$', 'autre', 's', ha='left')
save(fig, '74-096')
