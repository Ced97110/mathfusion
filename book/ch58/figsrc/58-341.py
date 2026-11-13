import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
# stocks (x, y) de 0 à 6 : pleins quand x + y est pair
ux = 9.5
ox, oy = 12, 14
N = 6
arrow(ax, (ox - 3, oy), (ox + N * ux + 5, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 3), (ox, oy + N * ux + 5), 'fixe', lw=0.7)
text(ax, ox + N * ux + 3, oy - 3.5, r'$x$', 'fixe', 's')
text(ax, ox - 3.5, oy + N * ux + 4, r'$y$', 'fixe', 's')
special = {(1, 1), (3, 5), (1, 2)}
for x in range(N + 1):
    for y in range(N + 1):
        px, py = ox + x * ux, oy + y * ux
        if (x, y) in special: continue
        if (x + y) % 2 == 0: disc(ax, px, py, 1.5, 'sujet')
        else: disc(ax, px, py, 0.6, 'fixe')
for (x, y), role, lab in (((1, 1), 'resultat', '(1, 1) : 2'), ((3, 5), 'resultat', '(3, 5) : 8'), ((1, 2), 'limite', '(1, 2) : 3')):
    px, py = ox + x * ux, oy + y * ux
    disc(ax, px, py, 2.0, role)
    text(ax, px + 2.8, py + 3.8, lab, role, 's', ha='left')
text(ax, 60, 77, 'x + y pair : disque plein', 'sujet', 's')
text(ax, 60, 83, 'sous-module', 'sujet', 'm', weight='bold')
save(fig, '58-341')
