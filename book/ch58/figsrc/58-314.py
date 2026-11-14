import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# colonne de la preuve
box(ax, 2, 58, 44, 14, 'sujet', label='1. c·η(v) = 0\nc·(1, 2) = (0, 0)', size='s')
arrow(ax, (24, 58), (24, 47), 'varie')
box(ax, 2, 33, 44, 13, 'varie', label='2. étape clé : c·(1, 0)\nest dans le noyau', size='s', weight='bold')
arrow(ax, (24, 33), (24, 22), 'varie')
box(ax, 2, 6, 44, 15, 'resultat', label='3. c·(1, 0) = a·(2, −1)\nbase de ℝ² : c = 0, a = 0', size='s')
line(ax, [(49, 6), (49, 72)], 'fixe', lw=0.5, dash=True)
# la figure : deux droites qui ne se coupent qu'en O
u = 5.0; ox, oy = 68, 40
p = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [p(-3, 0), p(3, 0)], 'varie', lw=1.4)
line(ax, [p(-3, 1.5), p(3, -1.5)], 'sujet', lw=1.4)
disc(ax, ox, oy, 1.4, 'resultat')
text(ax, 68, 68, 'deux droites', 'fixe', 's')
text(ax, p(2.2, 0)[0], p(2.2, 0)[1] + 3.5, 'multiples de v', 'varie', 's')
text(ax, p(2, -1)[0] - 1, p(2, -1)[1] - 4, 'noyau', 'sujet', 's')
text(ax, 68, 24, 'seul point commun : O', 'resultat', 's')
save(fig, '58-314')
