import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
box(ax, 3, 18, 26, 16, 'sujet'); text(ax, 16, 29, r'$G$', 'sujet', 'm'); text(ax, 16, 23, 'horloge', 'sujet', 's')
box(ax, 59, 18, 26, 16, 'autre'); text(ax, 72, 29, r"$G'$", 'autre', 'm'); text(ax, 72, 23, 'rotations', 'autre', 's')
arrow(ax, (30, 26), (58, 26), 'varie', lw=1.4)
text(ax, 44, 30, r'au moins un $\eta$', 'varie', 's')
text(ax, 44, 8, r'$G\cong G^{\prime}$', 'resultat', 'xl')
save(fig, '45-027')
