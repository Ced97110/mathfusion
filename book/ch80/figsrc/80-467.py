import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
text(ax, 22, 59, 'plan', 'encre', 'm', weight='bold'); text(ax, 68, 59, 'photo de rails', 'encre', 'm', weight='bold')
line(ax, [(8, 14), (38, 44)], 'sujet', lw=1.2); line(ax, [(8, 28), (24, 44)], 'autre', lw=1.2)
text(ax, 40, 49, r'$x-y=0$', 'sujet', 's'); text(ax, 14, 49, r'$x-y=-1$', 'autre', 's')
text(ax, 22, 6, 'jamais de point commun', 'limite', 's')
line(ax, [(50, 52), (86, 52)], 'fixe', dash=True)
line(ax, [(54, 8), (68, 52)], 'sujet', lw=1.2); line(ax, [(82, 8), (68, 52)], 'autre', lw=1.2)
disc(ax, 68, 52, 1.8, 'resultat')
text(ax, 68, 56, 'horizon', 'resultat', 's')
text(ax, 68, 4, 'ils se rejoignent', 'resultat', 's')
save(fig, '80-467')
