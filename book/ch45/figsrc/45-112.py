import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 4, 46, 80, 12, 'fixe', label=r'$((a_{1}a_{2})a_{3})a_{4}$', size='m')
text(ax, 44, 61.5, '3 combinaisons', 'fixe', 's'); text(ax, 44, 42, '2 paires de parenthèses', 'fixe', 's')
arrow(ax, (44, 38), (44, 30), 'varie'); text(ax, 48, 34, 'on les enlève', 'varie', 's', ha='left')
box(ax, 4, 16, 80, 12, 'resultat', label=r'$a_{1}a_{2}a_{3}a_{4}$', size='m')
text(ax, 44, 9, r'pour $n$ éléments : $n-2$ paires en moins', 'resultat', 's')
save(fig, '45-112')
