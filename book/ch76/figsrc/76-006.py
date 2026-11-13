import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
k = 0.42
vals = [(12, 'sujet'), (60, 'varie'), (120, 'resultat')]
ys = [66, 44, 22]
for (v, r), y in zip(vals, ys):
    ax.add_patch(Rectangle((3, y), v * k, 6, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))
    text(ax, 3 + v * k + 1.5, y + 3, f'{v}', r, 'm', ha='left')
for i, f in enumerate(['5', '2']):
    y = ys[i] - 2; arrow(ax, (6, y), (6, ys[i + 1] + 8), 'varie')
    text(ax, 9, (y + ys[i + 1] + 8) / 2, rf'$\times {f}$', 'varie', 'm', ha='left')
arrow(ax, (76, ys[0] + 3), (76, ys[2] + 3), 'resultat', lw=1.3)
text(ax, 73, 44, r'$\times 10$', 'resultat', 'm', ha='right'); text(ax, 73, 39.5, r'$=5\times 2$', 'resultat', 'm', ha='right')
save(fig, '76-006')
