import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 63, 'trois calculs en même temps', 'fixe', 's')
for x, m, a, b, r in [(2, 3, 1, 2, 2), (31, 4, 3, 0, 0), (60, 5, 2, 3, 1)]:
    box(ax, x, 24, 26, 30, 'sujet')
    text(ax, x + 13, 48, f'modulo {m}', 'sujet', 'm', weight='bold')
    text(ax, x + 13, 38, f'{a} × {b} = {r}', 'varie', 'm')
    text(ax, x + 13, 29, f'seulement {a} et {b}', 'fixe', 's')
text(ax, 44, 14, 'aucun lien entre les trois', 'encre', 's')
save(fig, '52-246')
