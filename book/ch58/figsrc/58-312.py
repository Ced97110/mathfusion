import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ul, ur = 8.0, 5.5
oxl, oyl = 12, 36
oxr, oyr = 58, 20
pl = lambda x, y: (oxl + x * ul, oyl + y * ul)
pr = lambda x, y: (oxr + x * ur, oyr + y * ur)
text(ax, 22, 52, r'base $(k, v)$ du plan', 'fixe', 's')
text(ax, 66, 52, 'images par $\\eta$', 'fixe', 's')
# départ : base du noyau (k) complétée par v
line(ax, [pl(-0.4, 0.2), pl(2.6, -1.3)], 'sujet', lw=0.6, dash=True)
arrow(ax, pl(0, 0), pl(2, -1), 'sujet', lw=1.8)
arrow(ax, pl(0, 0), pl(1, 0), 'varie', lw=1.8)
text(ax, pl(2, -1)[0], pl(2, -1)[1] - 4, 'k = (2, −1)', 'sujet', 's')
text(ax, pl(1, 0)[0] - 3, pl(1, 0)[1] + 5, 'v = (1, 0)', 'varie', 's')
# arrivée : k part en 0, v donne la base de l'image
line(ax, [pr(-0.4, -0.8), pr(1.5, 3.0)], 'resultat', lw=0.6, dash=True)
arrow(ax, pr(0, 0), pr(1, 2), 'resultat', lw=1.8)
disc(ax, oxr, oyr, 1.1, 'sujet')
text(ax, oxr + 4, oyr - 2.5, 'η(k) = (0, 0)', 'sujet', 's', ha='left')
text(ax, pr(1, 2)[0] + 3, pr(1, 2)[1] + 1, 'η(v) = (1, 2)', 'resultat', 's', ha='left')
arrow(ax, (36, 35), (48, 29), 'encre', lw=1.0)
text(ax, 42, 36.5, r'$\eta$', 'encre', 'm')
box(ax, 2, 1, 84, 8, 'resultat', label='η(v) seul : base de l’image', size='s')
save(fig, '58-312')
