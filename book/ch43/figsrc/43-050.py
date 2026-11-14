import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 6, 24, 26, 16, 'sujet', label=r'$A$', size='l')
box(ax, 56, 24, 26, 16, 'autre', label=r'$B$', size='l')
arrow(ax, (33, 32), (55, 32), 'varie')
text(ax, 44, 48, r'$P\,A\,P^{-1}=B$', 'varie', 'm')
text(ax, 44, 13, r'$A\sim B$', 'resultat', 'l')
text(ax, 44, 5, r'au moins un $P$ inversible', 'encre', 's')
save(fig, '43-050')
