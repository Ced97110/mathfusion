import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'$\nu : G \to G/K$', 'varie', 14)
text(ax, 17, 43, r'$G$', 'sujet', 's'); text(ax, 70, 43, r'$G/K$', 'resultat', 's')
disc(ax, 17, 26, 6, 'sujet', label='7')
box(ax, 48, 12, 38, 28, 'resultat', label='')
text(ax, 67, 33, '7 + 4ℤ', 'resultat'); text(ax, 67, 20, '3, 7, 11, …', 'resultat', 's')
arrow(ax, (24, 26), (47, 26), 'varie'); text(ax, 35.5, 31, r'$a\mapsto aK$', 'varie', 's')
save(fig, '48-032')
