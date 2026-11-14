import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 14; x0, y0 = 6, 20
cells = {'a': (0, 1, '3', 'sujet'), 'b': (1, 1, '1', 'varie'), 'c': (0, 0, '2', 'varie'), 'd': (1, 0, '2', 'sujet')}
for k, (i, j, v, role) in cells.items():
    box(ax, x0 + i * s, y0 + j * s, s - 1.5, s - 1.5, role)
    text(ax, x0 + i * s + (s - 1.5) / 2, y0 + j * s + (s - 1.5) / 2 + 1.6, v, role, 'l')
    text(ax, x0 + i * s + (s - 1.5) / 2, y0 + j * s + 2.6, k, role, 's')
arrow(ax, (x0 + 1.5, y0 + 2 * s - 2.2), (x0 + 2 * s - 3, y0 + 1.5), 'sujet', lw=0.6) if False else None
text(ax, 20, 8, 'ad − bc', 'resultat', 'l')
text(ax, 62, 46, '3 × 2 = 6', 'sujet', 'm'); text(ax, 62, 33, '1 × 2 = 2', 'varie', 'm')
text(ax, 62, 17, '6 − 2 = 4', 'resultat', 'l')
arrow(ax, (x0 + 2 * s - 1.5, y0 + s + 5), (47, 46), 'sujet', curve=0.0)
arrow(ax, (x0 + 2 * s - 1.5, y0 + s + 2), (47, 34), 'varie')
arrow(ax, (62, 29), (62, 21.5), 'resultat')
save(fig, '48-134')
