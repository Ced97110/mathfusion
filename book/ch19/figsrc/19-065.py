import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ox, oy, ux, uy = 8, 10, 9.6, 6.0
P = lambda x, y: (ox + x * ux, oy + y * uy)
arrow(ax, (ox, oy), (ox + 5.6 * ux, oy), 'fixe', lw=0.9)
line(ax, [P(0, 0), P(5, 10)], 'sujet', lw=1.4)
for a, b, d in [(5, 10, 2.2), (2, 4, 2.2), (1, 2, 2.2)]:
    poly(ax, [P(0, 0), P(a, 0), P(a, b)], 'varie', fill=False, lw=1.0)
    text(ax, ox + a * ux + 2.6, oy + b * uy / 2, str(b), 'varie', 's')
    text(ax, ox + a * ux, oy - 3, str(a), 'fixe', 's')
text(ax, 22, 48, 'même droite', 'sujet', 's')
for i, (a, b) in enumerate([(1, 2), (2, 4), (5, 10)]):
    text(ax, 74, 56 - i * 12, f'{b} sur {a} = 2', 'resultat', 'm')
text(ax, 74, 20, 'même rapport', 'resultat', 's')
save(fig, '19-065')
