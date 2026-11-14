import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, u = 16, 10, 40
poly(ax, [(ox, oy), (ox + u, oy), (ox + u, oy + u), (ox, oy + u)], 'sujet')
arrow(ax, (ox, oy), (ox + u + 8, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy), (ox, oy + u + 8), 'fixe', lw=0.8)
for i in range(6):
    for j in range(6):
        disc(ax, ox + 4 + i * 6.4, oy + 4 + j * 6.4, 0.9, 'sujet')
text(ax, ox + u + 8, oy - 3, r'$x$', 'fixe', 's'); text(ax, ox - 4, oy + u + 8, r'$v$', 'fixe', 's')
text(ax, ox, oy - 3, '0', 'fixe', 's'); text(ax, ox + u, oy - 3, '1', 'fixe', 's'); text(ax, ox - 3, oy + u, '1', 'fixe', 's')
text(ax, 72, 48, 'nuage', 'sujet', 's'); text(ax, 72, 44, 'de billes', 'sujet', 's')
text(ax, 72, 30, 'aire', 'resultat', 'm'); text(ax, 72, 25, r'$1 \times 1 = 1$', 'resultat', 's')
save(fig, '75-003')
