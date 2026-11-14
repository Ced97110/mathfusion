import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
u = 7.0; ul = 7.0
oxl, oyl = 8, 14
oxr, oyr = 50, 14
pl = lambda x, y: (oxl + x * ul, oyl + y * ul)
pr = lambda x, y: (oxr + x * u, oyr + y * u)
text(ax, 44, 42, r'$\eta(x,\ y) = (2x,\ 3y)$', 'encre', 'm')
for o in ((oxl, oyl), (oxr, oyr)):
    line(ax, [(o[0] - 2, o[1]), (o[0] + 26, o[1])], 'fixe', lw=0.5)
    line(ax, [(o[0], o[1] - 2), (o[0], o[1] + 21)], 'fixe', lw=0.5)
# départ
arrow(ax, pl(0, 0), pl(1, 0), 'sujet', lw=1.6)
arrow(ax, pl(0, 0), pl(0, 1), 'varie', lw=1.6)
arrow(ax, pl(0, 0), pl(1, 1), 'resultat', lw=1.6)
text(ax, pl(1, 0)[0] + 1, pl(1, 0)[1] - 3, '(1, 0)', 'sujet', 's', ha='left')
text(ax, pl(0, 1)[0] - 6, pl(0, 1)[1] + 3, '(0, 1)', 'varie', 's', ha='left')
text(ax, pl(1, 1)[0] + 1, pl(1, 1)[1] + 1, '(1, 1)', 'resultat', 's', ha='left')
# arrivée
arrow(ax, pr(0, 0), pr(2, 0), 'sujet', lw=1.6)
arrow(ax, pr(0, 0), pr(0, 3), 'varie', lw=1.6)
arrow(ax, pr(0, 0), pr(2, 3), 'resultat', lw=1.6)
line(ax, [pr(2, 0), pr(2, 3), pr(0, 3)], 'fixe', lw=0.7, dash=True)
text(ax, pr(2, 0)[0] + 1, pr(2, 0)[1] - 3, '(2, 0)', 'sujet', 's', ha='left')
text(ax, pr(0, 3)[0] - 1, pr(0, 3)[1] + 3, '(0, 3)', 'varie', 's', ha='left')
text(ax, pr(2, 3)[0] + 2, pr(2, 3)[1] + 3, '(2, 3)', 'resultat', 's', ha='left')
arrow(ax, (27, 22), (44, 22), 'encre', lw=1.0)
text(ax, 35.5, 25, r'$\eta$', 'encre', 'm')
box(ax, 2, 1, 84, 7, 'resultat', label='la somme est conservée : (2, 0) + (0, 3) = (2, 3)', size='s')
save(fig, '58-311')
