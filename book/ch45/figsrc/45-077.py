import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 4, 46, 20, 14, 'sujet', label=r'$a$', size='xl'); text(ax, 30, 53, '+', 'encre', 'l'); box(ax, 36, 46, 20, 14, 'varie', label=r'$L$', size='xl')
text(ax, 62, 53, '=', 'encre', 'l'); box(ax, 68, 46, 18, 14, 'resultat', label=r'$a_L$', size='xl')
text(ax, 14, 38, 'élément', 'sujet', 's'); text(ax, 46, 38, 'left : à gauche', 'varie', 's'); text(ax, 77, 38, 'application', 'resultat', 's')
box(ax, 4, 8, 80, 18, 'resultat', fill=False, label=r'$a_L : x \mapsto a\,x$', size='l')
text(ax, 44, 30, 'a est placé à gauche de x', 'encre', 's')
save(fig, '45-077')
