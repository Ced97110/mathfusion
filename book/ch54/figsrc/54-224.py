import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# at random: the criterion rarely applies
box(ax, 2, 58, 26, 11, 'fixe', label=r'$x^2+x+1$', size='m')
arrow(ax, (28.5, 63.5), (33, 63.5), 'fixe')
text(ax, 34, 66, 'aucun premier ne divise 1', 'fixe', 's', ha='left')
text(ax, 34, 61, 'critère inutilisable', 'fixe', 's', ha='left')
line(ax, [(2, 50), (86, 50)], 'fixe', dash=True, lw=0.6)
# by design: coefficients chosen so that the three conditions hold
box(ax, 2, 30, 26, 11, 'sujet', label=r'$x^3-2$', size='m')
for i, v in enumerate(['1', '0', '0', '−2']):
    box(ax, 33 + i * 13, 30, 12, 11, 'sujet', label=v, size='m')
text(ax, 59, 25, 'on choisit p = 2', 'sujet', 's')
arrow(ax, (44, 22), (44, 17), 'resultat')
box(ax, 2, 5, 84, 11, 'resultat', label=r'irréductible : $x^n-2$, tout degré $n$', size='m')
save(fig, '54-224')
