import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, sx, sy = 16, 12, 9, 11
arrow(ax, (ox, oy), (78, oy), 'fixe'); arrow(ax, (ox, oy), (ox, 50), 'fixe')
for (a, b, r, lab, dy) in [(3, 2, 'sujet', r'$3+2i$', 4), (5, 1, 'autre', r'$5+i$', 4)]:
    X, Y = ox + a * sx, oy + b * sy
    line(ax, [(X, oy), (X, Y), (ox, Y)], 'fixe', lw=0.6, dash=True)
    disc(ax, X, Y, 1.5, r)
    text(ax, X, Y + dy, lab, r)
    text(ax, X, oy - 3.5, str(a), 'varie', 's'); text(ax, ox - 3.5, Y, str(b), 'varie', 's')
text(ax, 52, 5, 'coefficient de 1', 'fixe', 's')
text(ax, 4, 32, r'coefficient de $i$', 'fixe', 's', rot=90)
text(ax, 44, 60, r'2 réels : briques 1 et $i$', 'sujet', 'l', weight='bold')
save(fig, '61-047')
