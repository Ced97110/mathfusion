import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# left : b real, one point
text(ax, 22, 54, 'si b est réel', 'sujet', 's', weight='bold')
line(ax, [(6, 12), (38, 12)], 'fixe')
line(ax, [(22, 12), (22, 46)], 'varie', dash=True)
text(ax, 22, 49.5, 'position 0', 'varie', 's')
disc(ax, 22, 29, 1.7, 'sujet'); text(ax, 30, 29, r'$b=\bar{b}$', 'sujet', 'm')
text(ax, 22, 5, 'un seul point', 'sujet', 's')
# right : b not real, two points
text(ax, 66, 54, 'si b n’est pas réel', 'sujet', 's', weight='bold')
line(ax, [(50, 12), (82, 12)], 'fixe')
line(ax, [(66, 12), (66, 46)], 'varie', dash=True)
text(ax, 66, 49.5, 'position 0', 'varie', 's')
disc(ax, 66, 37, 1.7, 'sujet'); text(ax, 70, 37, r'$b$', 'sujet', 'm')
disc(ax, 66, 21, 1.7, 'autre'); text(ax, 70.5, 21, r'$\bar{b}$', 'autre', 'm')
text(ax, 66, 5, r'$\bar{b}\neq b$ : deux points', 'autre', 's')
save(fig, '70-158')
