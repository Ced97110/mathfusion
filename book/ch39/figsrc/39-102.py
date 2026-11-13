import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

cx, cy, r = 44, 44, 25
fig, ax = canvas(92)
arrow(ax, (6, cy), (84, cy), 'fixe', lw=0.6)
arrow(ax, (cx, 12), (cx, 80), 'fixe', lw=0.6)
disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.6)
pts = [(cx + r * math.cos(math.radians(60 * k)), cy + r * math.sin(math.radians(60 * k))) for k in range(6)]
poly(ax, pts, 'sujet', fill=True, lw=1.0)
# projections de ω
w = pts[1]
line(ax, [w, (w[0], cy)], 'varie', lw=0.9, dash=True)
ax.add_patch(Arc((cx, cy), 16, 16, theta1=0, theta2=60, ec=COL['varie'], lw=1.1, zorder=3))
text(ax, cx + 4.5, cy - 3.5, '60°', 'varie', 's')
text(ax, w[0], cy - 3, '1/2', 'varie', 's')
text(ax, w[0] + 1.2, cy + 10, r'$\sqrt{3}/2$', 'varie', 's', ha='left')
for k in range(6):
    disc(ax, pts[k][0], pts[k][1], 1.4, 'sujet')
labs = ['1', r'$\omega$', r'$\omega^2$', r'$\omega^3$', r'$\omega^4$', r'$\omega^5$']
offs = [(3, 3, 'left'), (2, 3.5, 'left'), (-2, 3.5, 'right'), (-3, 3, 'right'), (-2, -3.5, 'right'), (2, -3.5, 'left')]
for k in range(6):
    text(ax, pts[k][0] + offs[k][0], pts[k][1] + offs[k][1], labs[k], 'sujet', 'm', ha=offs[k][2])
text(ax, 4, 87, r'$n=6$', 'encre', 'l', ha='left')
text(ax, 84, 87, r'$\omega=\frac{1}{2}+\frac{\sqrt{3}}{2}\,i$', 'sujet', 's', ha='right')
save(fig, '39-102')
