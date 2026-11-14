import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(80)
xs, p = bitrow(fig, ax, 54, 24, '01234567', 'fixe', 'l', 5)
text(ax, 2, 24, 'pas k', 'fixe', 's', ha='left')
text(ax, 2, 62, '1', 'sujet', 'l', ha='left')
text(ax, 2, 42, 'α', 'sujet', 'l', ha='left')
for k, x in enumerate(xs):
    disc(ax, x, 62, 2.6, 'resultat')
    disc(ax, x, 42, 2.6, 'resultat' if k in (0, 7) else 'fixe', fill=k in (0, 7))
text(ax, 54, 53, 'déjà 1 au pas 1 : pas primitive', 'limite', 's')
text(ax, 54, 33, 'seulement au pas 7 : primitive', 'resultat', 's')
text(ax, 44, 10, 'plein : la puissance vaut 1', 'encre', 's')
save(fig, '68-205')
