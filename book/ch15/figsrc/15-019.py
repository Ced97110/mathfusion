import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'équation', 'sujet', 'l')
box(ax, 5, 36, 36, 11, 'sujet', label=r'$6n+40$'); text(ax, 47, 41.5, '=', 'varie', 'l')
box(ax, 53, 36, 30, 11, 'sujet', label=r'$100$')
text(ax, 23, 30, 'expression', 'fixe', 's'); text(ax, 68, 30, 'expression', 'fixe', 's')
box(ax, 8, 6, 72, 11, 'resultat', label=r'$6 \times 10 + 40 = 100$')
text(ax, 44, 22, 'pour 10 personnes', 'resultat', 's')
save(fig, '15-019')
