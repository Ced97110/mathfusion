import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(1, 12, 0), (2, 19, -1), (3, 27, 1)]
ys = [50, 38, 26]
for (n, g, m), y in zip(rows, ys):
    box(ax, 2, y, 25, 8, 'fixe', label=f'contrôle {n}')
    box(ax, 30, y, 17, 8, 'sujet', label=f'$g$ = {g}')
    box(ax, 50, y, 14, 8, 'varie', label=r'$\times$ ' + ('(−1)' if m < 0 else f'{m}'))
    box(ax, 67, y, 19, 8, 'fixe', label=f'= {g * m}'.replace('-', '−'.strip()))
for y in ys: arrow(ax, (47, y + 4), (50, y + 4), 'fixe', lw=0.6)
text(ax, 20, 12, 'additionner les 3', 'varie', 's')
arrow(ax, (76, 25), (76, 17), 'varie')
box(ax, 34, 6, 52, 10, 'resultat', label=r'$f(3)=0-19+27=8$')
text(ax, 17, 56 + 4, '', 'encre', 's')
save(fig, '80-265')
