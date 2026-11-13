import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(70)
Y0 = 14
f = numberline(ax, 10, 76, Y0, -1, 2, 1, arrow_right=False)
xs = np.linspace(-1, 2, 120)
ys = xs ** 3 - xs
ax.plot([f(v) for v in xs], [Y0 + 6.5 * v for v in ys], color=COL['sujet'], lw=1.4, zorder=3)
for v in (0, 1, 2):
    ax.add_patch(Rectangle((f(v) - 1.8, Y0 - 1.8), 3.6, 3.6, ec=COL['resultat'], fc=FILL['resultat'], lw=0.9, zorder=2))
for v, h in ((0, 0), (1, 0), (2, 6)):
    disc(ax, f(v), Y0 + 6.5 * h, 1.1, 'varie')
arrow(ax, (f(2), Y0 + 6.5 * 6 - 3), (f(2), Y0 + 3.5), 'varie')
text(ax, f(2) + 3, Y0 + 6.5 * 6, '6', 'varie', 's', ha='left')
text(ax, f(2) + 2.5, 32, r'$6\to0$', 'varie', 's', ha='left')
text(ax, 4, 64, r'courbe $x^3-x$ sur $\mathbb{R}$', 'sujet', 's', ha='left')
text(ax, 4, 3.5, r'carrés : valeurs dans $\mathbb{Z}/3\mathbb{Z}$', 'resultat', 's', ha='left')
save(fig, '55-011')
