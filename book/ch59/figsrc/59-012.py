import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# tableau des quatre cases, au centre en haut
for (r, c, v) in [(0, 0, 4), (0, 1, 6), (1, 0, 6), (1, 1, 4)]:
    box(ax, 33 + c * 11, 54 - r * 11, 10, 10, 'sujet', label=str(v), size='m')
text(ax, 44, 70.5, 'les 4 cases du tableau', 'sujet', 's')
# deux nombres calculés à partir des cases
box(ax, 2, 28, 40, 10, 'fixe', label='PGCD des cases = 2', size='s')
box(ax, 46, 28, 40, 10, 'fixe', label=r'$|$déterminant$|$ = 20', size='s')
arrow(ax, (36, 42), (22, 39), 'fixe'); arrow(ax, (52, 42), (66, 39), 'fixe')
# ce que portent les facteurs invariants
box(ax, 2, 4, 40, 14, 'resultat', label=r'$d_1=2$ : le PGCD', size='s')
box(ax, 46, 4, 40, 14, 'resultat', label=r'$d_1\times d_2=2\times10=20$', size='s')
arrow(ax, (22, 27), (22, 19.5), 'varie'); arrow(ax, (66, 27), (66, 19.5), 'varie')
save(fig, '59-012')
