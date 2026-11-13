import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# 41-031 : a = ‖v‖ cos θ : relever 100 et 60° -> cos 60° = 0,5 -> 100 × 0,5 = 50
fig, ax = canvas(66)
steps = [('1  relever 100 et 60°', 'fixe'), ('2  cos 60° = 0,5', 'varie'), ('3  100 × 0,5 = 50', 'resultat')]
bx, bw, bh = 3, 41, 13
ys = [48, 29, 10]
for (lab, role), y in zip(steps, ys):
    box(ax, bx, y, bw, bh, role, label=lab, size='m')
for y_hi, y_lo in zip(ys[:-1], ys[1:]):
    arrow(ax, (bx + bw / 2, y_hi - 0.3), (bx + bw / 2, y_lo + bh + 0.3), 'fixe', lw=1.0)
# triangle du vent, échelle 0,4 mm par unité : côté adjacent = 50 = 100 × 0,5
s = 0.4
O = (52, 14)
V = (O[0] + 50 * s, O[1] + 86.6 * s)
P = (V[0], O[1])
line(ax, [V, P], 'fixe', dash=True)
line(ax, [O, P], 'resultat', lw=2.0)
arrow(ax, O, V, 'varie', lw=1.4)
ax.add_patch(Arc(O, 12, 12, theta1=0, theta2=60, ec=COL['fixe'], lw=1.0, zorder=3))
text(ax, O[0] + 11, O[1] + 3.2, '60°', 'fixe', 's')
text(ax, (O[0] + P[0]) / 2, O[1] - 3.5, '$a$ = 50', 'resultat', 'm')
text(ax, (O[0] + V[0]) / 2 - 2.5, (O[1] + V[1]) / 2 + 2.5, '100', 'varie', 'm', ha='right')
save(fig, '41-031')
