import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
brace(ax, 3, 55, 36, 'encre', label=r'$P^TAP$', down=False, size='m')
box(ax, 3, 8, 16, 22, 'fixe', label=r'$P^T$', size='l')
box(ax, 21, 8, 16, 22, 'sujet', label=r'$A$', size='l')
box(ax, 39, 8, 16, 22, 'varie', label=r'$P$', size='l')
text(ax, 59.5, 19, '=', 'encre', 'l')
box(ax, 64, 8, 21, 22, 'resultat', label=r"$A'$", size='l')
text(ax, 11, 3.5, 'transposée\nde P', 'fixe', 's'); text(ax, 29, 3.5, 'ancienne\nbase', 'sujet', 's')
text(ax, 47, 3.5, 'matrice de\npassage', 'varie', 's'); text(ax, 74.5, 3.5, 'nouvelle\nbase', 'resultat', 's')
save(fig, '71-137')
