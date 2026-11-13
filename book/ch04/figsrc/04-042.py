import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(80)

# ligne du haut : √ est un signe, 16 le radicande, 4 la racine
line(ax, [(8, 54), (10, 55.5), (13, 47), (16, 62), (32, 62)], 'fixe', lw=1.4)
text(ax, 16, 70, 'radical : un signe', 'fixe', 's')
text(ax, 24, 55, '16', 'autre', 'l')
text(ax, 24, 41, 'radicande : donné', 'autre', 's')
text(ax, 38, 55, '=', 'encre', 'l')
box(ax, 41, 50, 8, 10, 'sujet', fill=False)
text(ax, 45, 55, '4', 'sujet', 'l', weight='bold')
text(ax, 45, 70, 'racine : trouvé', 'sujet', 's')

# contrôle : on multiplie la racine par elle-même
arrow(ax, (49, 55), (59, 55), 'varie', lw=1.0)
text(ax, 70, 55, '4 × 4 = 16', 'varie', 'l')
text(ax, 70, 47, 'pas 16 × 16', 'limite', 's')

# ligne du bas : ∛8 = 2
line(ax, [(8, 20), (10, 21.5), (13, 13), (16, 28), (28, 28)], 'fixe', lw=1.4)
text(ax, 10.5, 25, '3', 'fixe', 's')
text(ax, 22, 21, '8', 'autre', 'l')
text(ax, 34, 21, '=', 'encre', 'l')
box(ax, 37, 16, 8, 10, 'sujet', fill=False)
text(ax, 41, 21, '2', 'sujet', 'l', weight='bold')
arrow(ax, (45, 21), (55, 21), 'varie', lw=1.0)
text(ax, 68, 21, '2 × 2 × 2 = 8', 'varie', 'm')

save(fig, '04-042')
