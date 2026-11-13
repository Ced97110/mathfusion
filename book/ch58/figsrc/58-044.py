import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# gauche : (1, 0) et (2, 0), sur la même droite
text(ax, 22, 64, 'pas indépendants', 'limite', 'm')
arrow(ax, (6, 40), (30, 40), 'sujet', lw=1.4)            # (2, 0)
arrow(ax, (6, 49), (18, 49), 'sujet', lw=1.4)            # (1, 0)
text(ax, 34, 40, '(2, 0)', 'sujet', 's', ha='left')
text(ax, 22, 53, '(1, 0)', 'sujet', 's')
box(ax, 2, 14, 40, 12, 'limite', label=r'$2\times(1,0)-(2,0)=(0,0)$', size='s')
text(ax, 22, 8, 'coefficients 2 et −1', 'limite', 's')
# droite : (1, 0) et (0, 1), directions différentes
text(ax, 66, 64, 'indépendants', 'resultat', 'm')
arrow(ax, (52, 36), (70, 36), 'sujet', lw=1.4)           # (1, 0)
arrow(ax, (52, 36), (52, 54), 'sujet', lw=1.4)           # (0, 1)
text(ax, 77, 36, '(1, 0)', 'sujet', 's', ha='left')
text(ax, 58, 54, '(0, 1)', 'sujet', 's', ha='left')
box(ax, 46, 14, 40, 12, 'resultat', label=r'$0\times(1,0)+0\times(0,1)=(0,0)$', size='s')
text(ax, 66, 8, 'seulement 0 et 0', 'resultat', 's')
save(fig, '58-044')
