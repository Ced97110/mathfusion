import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 14
for ox, dx in ((8, 0), (50, 0)):
    oy = 24
    line(ax, [(ox - 3, oy), (ox + 30, oy)], 'fixe', lw=0.5, dash=True)
# gauche : (0, 1) hors de la droite de (1, 0)
ox, oy = 8, 24
arrow(ax, (ox, oy), (ox, oy + u), 'varie', lw=1.6)
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.6)
text(ax, ox + u / 2, oy - 4.5, r'$(1,\ 0)$', 'sujet', 's')
text(ax, ox + 9, oy + u - 1, r'$(0,\ 1)$', 'varie', 's')
text(ax, 22, 46, '(0, 1) hors de la droite', 'encre', 's')
box(ax, 2, 4, 40, 9, 'resultat', label='reste indépendante', size='s')
# droite : (2, 0) sur la droite
ox = 50
arrow(ax, (ox, oy), (ox + 2 * u, oy), 'varie', lw=1.6)
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=2.2)
text(ax, ox + u / 2, oy - 4.5, r'$(1,\ 0)$', 'sujet', 's')
text(ax, ox + 2 * u - 6, oy + 4.5, r'$(2,\ 0)$', 'varie', 's')
text(ax, 66, 46, '(2, 0) sur la droite', 'encre', 's')
box(ax, 46, 4, 40, 9, 'limite', label=r'liée : 2·(1, 0) − (2, 0) = 0', size='s')
save(fig, '58-301')
