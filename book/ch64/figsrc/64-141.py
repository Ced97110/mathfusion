import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, 'suite de composition', 'encre', 'm')
# largeurs proportionnelles aux tailles 120, 60, 1
box(ax, 4, 54, 60, 9, 'sujet', label=r'$S_5$ : 120')
box(ax, 4, 32, 30, 9, 'limite', label=r'$A_5$ : 60')
box(ax, 4, 10, 3, 9, 'fixe')
text(ax, 11, 14.5, r'$\{e\}$ : 1', 'fixe', 'm', ha='left')
arrow(ax, (6, 53.7), (6, 41.3), 'resultat')
arrow(ax, (5.5, 31.7), (5.5, 19.3), 'limite')
text(ax, 12, 47.5, 'facteur 2 : premier', 'resultat', 'm', ha='left')
text(ax, 12, 25.5, 'facteur 60 : pas premier', 'limite', 'm', ha='left')
text(ax, 44, 3, "Jordan-Hölder : toute suite\na les mêmes facteurs", 'encre', 's')
save(fig, '64-141')
