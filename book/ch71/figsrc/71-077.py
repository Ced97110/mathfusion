import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$x=(3,\,5)$ et $z=(2,\,-1)$', 'encre', 's')
rows = [(r'$x_1y_1$', 6), (r'$2x_1y_2$', -6), (r'$2x_2y_1$', 20), (r'$4x_2y_2$', -20)]
x0, k = 56, 1.0
for i, (n, v) in enumerate(rows):
    y = 54 - 10 * i
    text(ax, 2, y, n, 'fixe', 's', ha='left')
    role = 'sujet' if v > 0 else 'varie'
    xa, xb = (x0, x0 + v * k) if v > 0 else (x0 + v * k, x0)
    ax.add_patch(Rectangle((xa, y - 3), xb - xa, 6, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    s = f'+{v}' if v > 0 else f'−{-v}'
    if v > 0: text(ax, xb + 1, y, s, role, 's', ha='left')
    else: text(ax, xa - 1, y, s, role, 's', ha='right')
line(ax, [(x0, 62), (x0, 19)], 'encre', lw=0.8)
box(ax, 20, 2, 48, 8, 'resultat', label='somme = 0', size='m')
text(ax, 44, 14, r'chaque terme est annulé par un autre', 'resultat', 's')
save(fig, '71-077')
