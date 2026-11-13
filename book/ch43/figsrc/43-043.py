import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 8, 25, 18, 10, 'sujet', label='(1, 2)', size='s'); box(ax, 62, 25, 18, 10, 'autre', label='(3, 2)', size='s')
arrow(ax, (17, 35), (71, 35), 'varie', curve=-0.35); text(ax, 44, 48, r'$T_P$', 'varie', 'm')
arrow(ax, (71, 25), (17, 25), 'resultat', curve=-0.35); text(ax, 44, 11, r'$P^{-1}$ : retour', 'resultat', 'm')
text(ax, 44, 30, r'$P$ inversible', 'encre', 's')
save(fig, '43-043')
