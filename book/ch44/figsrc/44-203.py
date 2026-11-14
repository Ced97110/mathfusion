import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 14; h = s / 2
def sq(cx, cy, p, role='fixe'):
    poly(ax, [(cx-h, cy-h), (cx+h, cy-h), (cx+h, cy+h), (cx-h, cy+h)], role)
    dx, dy = [(-1, -1), (1, -1), (1, 1), (-1, 1)][p]
    ax.add_patch(Circle((cx + dx * h * 0.55, cy + dy * h * 0.55), 1.8, fc=COL['sujet'], ec=COL['sujet'], zorder=4))
xs = [14, 44, 74]
for cy, pos, ops, fin, role in [(50, [0, 1, 2], ['r', 's'], 'coin 1 en 3', 'resultat'), (22, [0, 3, 0], ['s', 'r'], 'coin 1 en 1', 'limite')]:
    for x, p in zip(xs, pos): sq(x, cy, p, role if x == 74 else 'fixe')
    for i, o in enumerate(ops):
        arrow(ax, (xs[i] + h + 1.5, cy), (xs[i + 1] - h - 1.5, cy), 'varie')
        text(ax, (xs[i] + xs[i + 1]) / 2, cy + 3.5, o, 'varie', 'm')
    text(ax, 74, cy - 11, fin, role, 's')
for p, (dx, dy) in enumerate([(-1, -1), (1, -1), (1, 1), (-1, 1)]):
    text(ax, 14 + dx * (h + 2.5), 50 + dy * (h + 2.5), str(p + 1), 'fixe', 's')
text(ax, 44, 36, r'$\neq$', 'limite', 'l')
text(ax, 20, 6, 'r : quart de tour', 'varie', 's'); text(ax, 66, 6, 's : retournement', 'varie', 's')
save(fig, '44-203')
