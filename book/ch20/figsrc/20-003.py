import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
for xx, s, r in [(12, r'$2x$', 'sujet'), (25, r'$+$', 'encre'), (38, r'$3y$', 'varie'), (55, r'$\leq$', 'encre'), (71, r'$12$', 'fixe')]:
    text(ax, xx, 52, s, r, 'xl', weight='bold')
for xx, s, r in [(12, 'dépense\ndes pains', 'sujet'), (38, 'dépense\ndes gâteaux', 'varie'), (55, 'au plus', 'encre'), (71, 'budget\nen euros', 'fixe')]:
    text(ax, xx, 40, s, r, 's')
text(ax, 2, 22, '3 pains, 2 gâteaux', 'encre', 'm', ha='left'); text(ax, 52, 22, r'$12\leq12$ : vrai', 'resultat', 'm', ha='left')
text(ax, 2, 10, '4 pains, 2 gâteaux', 'encre', 'm', ha='left'); text(ax, 52, 10, r'$14\leq12$ : faux', 'limite', 'm', ha='left')
save(fig, '20-003')
