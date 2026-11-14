import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'$a\times b=0$ : un facteur est nul', 'sujet', 'm')
rows = [(2, 3, 6), (5, 1, 5), (4, 0, 0)]
for i, (a, b, p) in enumerate(rows):
    y = 40 - 17 * i
    za, zb = a == 0, b == 0
    box(ax, 10, y, 14, 11, 'varie' if za else 'sujet', label=f'{a}')
    text(ax, 29, y + 5.5, r'$\times$')
    box(ax, 34, y, 14, 11, 'varie' if zb else 'sujet', label=f'{b}')
    box(ax, 54, y, 24, 11, 'resultat' if p == 0 else 'fixe', label=f'= {p}')
text(ax, 66, 40 - 17 * 2 - 4, 'facteur nul', 'varie', 's')
save(fig, '21-037')
