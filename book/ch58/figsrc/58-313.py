import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ul = 2.6
oxl, oyl = 28, 12
ur = 1.0
oxr, oyr = 64, 12
pl = lambda x, y: (oxl + x * ul, oyl + y * ul)
pr = lambda x, y: (oxr + x * ur, oyr + y * ur)
text(ax, 44, 60, '(3, 4) = −4·(2, −1) + 11·(1, 0)', 'encre', 's')
# départ : -4k puis 11v, somme (3, 4)
arrow(ax, pl(0, 0), pl(-8, 4), 'sujet', lw=1.5)
arrow(ax, pl(-8, 4), pl(3, 4), 'varie', lw=1.5)
arrow(ax, pl(0, 0), pl(3, 4), 'encre', lw=1.0)
text(ax, 3, 8, '−4k : noyau', 'sujet', 's', ha='left')
text(ax, pl(-3, 4)[0] + 2, pl(-3, 4)[1] + 4, '11v', 'varie', 's')
text(ax, pl(3, 4)[0] + 2, pl(3, 4)[1] - 1, '(3, 4)', 'encre', 's', ha='left')
# arrivée : le morceau du noyau disparaît
disc(ax, oxr, oyr, 1.1, 'sujet')
arrow(ax, pr(0, 0), pr(11, 22), 'varie', lw=1.5)
text(ax, oxr + 2, oyr - 4, 'η(−4k) = 0', 'sujet', 's', ha='left')
text(ax, pr(11, 22)[0] - 2, pr(11, 22)[1] + 4, 'η(3, 4) = (11, 22)', 'resultat', 's', ha='right')
text(ax, pr(11, 22)[0] + 2, pr(5, 11)[1], '11·η(v)', 'varie', 's', ha='left')
arrow(ax, (40, 40), (50, 40), 'encre', lw=1.0)
text(ax, 45, 44, r'$\eta$', 'encre', 'm')
save(fig, '58-313')
