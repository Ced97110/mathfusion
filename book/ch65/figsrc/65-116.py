import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cxs = (28, 52, 76)
text(ax, 44, 67, r'ce que fait chaque élément de $A_3$', 'fixe', 's')
for c, r in zip(cxs, (r'$1$', r'$\sigma$', r'$\sigma^2$')):
    box(ax, c - 10, 52, 20, 9, 'fixe', label=r, size='s')
text(ax, 7, 41.5, r'$z_1$', 'sujet', 'm')
text(ax, 7, 17.5, r'$z_1^3$', 'resultat', 'm')
for c, a in zip(cxs, (r'$z_1$', r'$w^2z_1$', r'$wz_1$')):
    box(ax, c - 10, 37, 20, 9, 'varie', label=a, size='s')
    arrow(ax, (c, 37), (c, 26), 'sujet')
    box(ax, c - 10, 13, 20, 9, 'resultat', label=r'$-111-60w$', size='s')
text(ax, cxs[1] + 2, 31, 'au cube', 'sujet', 's', ha='left')
text(ax, 44, 5, 'le cube ne bouge pas', 'resultat', 's')
save(fig, '65-116')
