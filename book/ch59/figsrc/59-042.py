import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 12, 10, 12
P = lambda a, b: (ox + a * u, oy + b * u)
for a in range(4):
    for b in range(5):
        disc(ax, *P(a, b), 0.5, 'fixe')
ax.add_patch(Polygon([P(0, 0), P(2, 3), P(3, 4), P(1, 1)], closed=True, ec=COL['varie'], fc=FILL['varie'], lw=0.8, alpha=0.8, zorder=1.5))
ax.add_patch(Polygon([P(0, 0), P(1, 0), P(1, 1), P(0, 1)], closed=True, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, alpha=0.9, zorder=1.6))
arrow(ax, P(0, 0), P(1, 0), 'fixe', lw=1.4); arrow(ax, P(0, 0), P(0, 1), 'fixe', lw=1.4)
arrow(ax, P(0, 0), P(2, 3), 'varie', lw=1.4); arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.4)
text(ax, *P(1.0, -0.4), r'$e_1$', 'fixe', 'm'); text(ax, *P(-0.45, 0.8), r'$e_2$', 'fixe', 'm')
text(ax, *P(1.9, 3.35), r"$e'_1$", 'varie', 'm'); text(ax, P(1, 1)[0] + 3.5, P(1, 1)[1] - 2.5, r"$e'_2$", 'varie', 'm')
text(ax, 86, 56, r"$e'_1=2e_1+3e_2$", 'varie', 'm', ha='right')
text(ax, 86, 48, r"$e'_2=1e_1+1e_2$", 'varie', 'm', ha='right')
text(ax, 86, 36, r'$P=(2\ 3;\ 1\ 1)$', 'varie', 'm', ha='right')
text(ax, 86, 28, r'$\det P=2\cdot1-3\cdot1=-1$', 'resultat', 's', ha='right')
save(fig, '59-042')
