import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(80)
text(ax, 2, 72, r'$x^6$', 'sujet', 's', ha='left')
brow(fig, ax, 58, 72, '0000001', role='sujet')
arrow(ax, (58, 67), (58, 57), 'varie')
text(ax, 61, 62, r'$\times\ x$', 'varie', 'm', ha='left')
text(ax, 2, 50, 'sans règle', 'limite', 's', ha='left')
brow(fig, ax, 58, 50, '00000001', roles=['fixe'] * 7 + ['limite'])
text(ax, 58, 42, 'x⁷ : 8 bits, hors du mot', 'limite', 's')
arrow(ax, (58, 38), (58, 28), 'varie')
text(ax, 61, 33, 'règle x⁷ = 1', 'varie', 's', ha='left')
text(ax, 2, 22, 'avec la règle', 'resultat', 's', ha='left')
brow(fig, ax, 58, 22, '1000000', role='resultat')
text(ax, 58, 11, 'le bit sorti revient en tête', 'resultat', 's')
save(fig, '68-185')
