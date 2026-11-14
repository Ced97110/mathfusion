import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 64, r'$S_n$', 'sujet', 16, weight='bold')
text(ax, 44, 55, r'$n$ = nombre de numéros', 'varie', 's')
def row(y, n, k):
    box(ax, 4, y, 20, 9, 'varie', label=rf'$n={n}$')
    arrow(ax, (24, y + 4.5), (32, y + 4.5), 'varie')
    box(ax, 32, y, 20, 9, 'sujet', label=rf'$S_{n}$')
    arrow(ax, (52, y + 4.5), (60, y + 4.5), 'sujet')
    box(ax, 60, y, 26, 9, 'resultat', label=f'{k} permutations', size='s')
row(36, 3, 6)
row(18, 4, 24)
text(ax, 44, 8, 'seul le nombre de numéros change', 'fixe', 's')
save(fig, '44-118')
