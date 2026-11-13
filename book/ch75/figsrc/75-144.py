import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
O = (22, 29); u = 13
arrow(ax, (6, O[1]), (57, O[1]), 'fixe', lw=0.8); arrow(ax, (O[0], 8), (O[0], 52), 'fixe', lw=0.8)
text(ax, 55, O[1] - 3, 'Re', 'fixe', 's'); text(ax, O[0] + 4, 50, 'Im', 'fixe', 's')
z = (O[0] + u, O[1] + u); zb = (O[0] + u, O[1] - u)
arrow(ax, O, (z[0] - 1, z[1] - 1), 'sujet', lw=1.2); arrow(ax, O, (zb[0] - 1, zb[1] + 1), 'autre', lw=1.2)
text(ax, z[0] + 3, z[1] + 2, r'$z=1+i$', 'sujet', 's', ha='left'); text(ax, zb[0] + 3, zb[1] - 2, r'$\bar z=1-i$', 'autre', 's', ha='left')
arrow(ax, (z[0], z[1] - 3), (zb[0], zb[1] + 3), 'varie', both=True)
text(ax, z[0] + 2, O[1] + 4.5, r'signe de $i$', 'varie', 's', ha='left')
box(ax, 62, 22, 24, 16, 'resultat'); text(ax, 74, 33, r'$z\bar z=2$', 'resultat', 'm'); text(ax, 74, 26.5, 'réel positif', 'resultat', 's')
save(fig, '75-144')
