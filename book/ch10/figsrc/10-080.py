import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
line(ax, [(8, 38), (82, 38)], 'fixe')
text(ax, 3, 38, '50', 'fixe', 'm', ha='left')
for cx, n, e in [(18, '48', -2), (34, '49', -1), (50, '51', 1), (66, '54', 4)]:
    h = 3.5 * e
    ax.add_patch(Rectangle((cx - 4.5, 38), 9, h, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
    text(ax, cx, 38 + h + (2.5 if e > 0 else -2.5), f'{e:+d}'.replace('-', '−'), 'varie', 'm')
    text(ax, cx, 24, n, 'fixe', 'm')
text(ax, 44, 16, 'somme des écarts = +2', 'varie', 'm')
text(ax, 44, 9.5, r'$E = 200 - 202 = -2$', 'resultat', 'm')
text(ax, 44, 3.5, 'même nombre, signe opposé', 'fixe', 's')
save(fig, '10-080')
