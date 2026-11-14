import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s = 9
x0, y0 = 6, 30
A = (x0, y0); B = (x0 + 5 * s, y0); C = (x0 + 1.8 * s, y0 + 2.4 * s)
poly(ax, [A, B, C], 'sujet')
line(ax, [A, B], 'sujet', lw=2.0)
line(ax, [C, (C[0], y0)], 'varie', lw=1.3, dash=True)
k = 2.0
line(ax, [(C[0], y0 + k), (C[0] + k, y0 + k), (C[0] + k, y0)], 'varie', lw=0.8)
text(ax, x0 + 2.5 * s, y0 - 4, '$b$ = 5', 'sujet', 's')
text(ax, C[0] + 9.5, y0 + 9, '$h$ = 2,4', 'varie', 's')
text(ax, 9, y0 + 15, '3', 'limite', 's')
text(ax, 37, y0 + 15, '4', 'limite', 's')
text(ax, 66, 52, 'côtés obliques', 'limite', 's')
text(ax, 66, 47, '3 et 4', 'limite', 's')
text(ax, 66, 40, 'hauteur : angle droit', 'varie', 's')
text(ax, 22, 18, '5 × 3 ÷ 2 = 7,5', 'limite', 'm')
text(ax, 22, 12, 'faux : 3 est oblique', 'limite', 's')
text(ax, 66, 18, '5 × 2,4 ÷ 2 = 6', 'resultat', 'm', weight='bold')
text(ax, 66, 12, 'juste : 2,4 est la hauteur', 'resultat', 's')
save(fig, '11-109')
