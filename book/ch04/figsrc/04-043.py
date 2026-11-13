import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(60)

text(ax, 22, 56, 'ce qu’on écrit', 'encre', 's')
text(ax, 66, 56, 'ce qu’on lit', 'encre', 's')

# ce qu'on écrit : √16, le creux est vide
line(ax, [(8, 38), (10, 39.5), (13, 31), (16, 46), (32, 46)], 'encre', lw=1.5)
text(ax, 24, 39, '16', 'encre', 'l')
ax.add_patch(Circle((10.5, 44), 2.5, ec=COL['sujet'], fc='none', lw=0.8, ls='--', zorder=2))
text(ax, 44, 40, 'veut dire', 'encre', 's')

# ce qu'on lit : ²√16, l'indice 2 rendu visible
line(ax, [(56, 38), (58, 39.5), (61, 31), (64, 46), (80, 46)], 'encre', lw=1.5)
text(ax, 72, 39, '16', 'encre', 'l')
text(ax, 58.5, 43.5, '2', 'sujet', 's', weight='bold')

text(ax, 44, 22, 'les deux : 2 facteurs égaux', 'resultat', 's')

# la remarque ne vaut que pour l'indice 2
line(ax, [(6, 10), (8, 11.5), (11, 3), (14, 16), (26, 16)], 'autre', lw=1.5)
text(ax, 8.6, 15, '3', 'autre', 's', weight='bold')
text(ax, 20, 9, '8', 'autre', 'l')
text(ax, 58, 9, 'indice 3 : toujours écrit', 'autre', 's')

save(fig, '04-043')
