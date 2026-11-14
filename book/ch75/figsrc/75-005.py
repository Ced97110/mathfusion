import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u, oy = 14, 14
for ox, shape, tt in [(8, [(0, 0), (1, 0), (1, 1), (0, 1)], 'carré'), (40, [(0, 0), (1, 0), (3, 1), (2, 1)], 'parallélogramme')]:
    poly(ax, [(ox + a * u, oy + b * u) for a, b in shape], 'sujet' if ox == 8 else 'resultat')
    text(ax, ox + (7 if ox == 8 else 21), oy + u + 7, tt, 'sujet' if ox == 8 else 'resultat', 's')
    text(ax, ox + 0.5 * u if ox == 8 else ox + 1.5 * u, oy + u / 2, 'aire 1', 'sujet' if ox == 8 else 'resultat', 's')
    text(ax, ox + 0.5 * u, oy - 4, 'base 1', 'fixe', 's')
ox = 40
line(ax, [(ox + 2 * u, oy + u), (ox + 2 * u, oy)], 'fixe', dash=True)
text(ax, ox + 2 * u + 2, oy + u / 2, 'hauteur 1', 'fixe', 's', ha='left')
arrow(ax, (26, oy + u / 2), (36, oy + u / 2), 'varie'); text(ax, 31, oy + u / 2 + 4, '2 s', 'varie', 's')
save(fig, '75-005')
