import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(85)
box(ax, 2, 70, 24, 10, 'sujet', label=r'$F$ : $n=16$', size='s')
box(ax, 32, 70, 24, 10, 'varie', label=r'ordre de 1 $=p$', size='s')
box(ax, 62, 70, 24, 10, 'resultat', label=r'$p\mid n$ : $2\mid16$', size='s')
arrow(ax, (26, 75), (32, 75), 'fixe')
arrow(ax, (56, 75), (62, 75), 'fixe')
text(ax, 14, 66, 'départ', 'sujet', 's')
text(ax, 44, 66, 'étape qui porte', 'varie', 's')
text(ax, 74, 66, 'arrivée', 'resultat', 's')
for row, cy in enumerate((50, 35)):
    for k in range(4):
        x0 = 4 + 21 * k
        first = (row == 0 and k == 0)
        ax.add_patch(Rectangle((x0, cy - 5), 17, 10, fc='none', ec=COL['sujet' if first else 'fixe'], lw=1.0, zorder=2))
        for dx in (4.5, 12.5):
            disc(ax, x0 + dx, cy, 3.5, 'sujet' if first else 'fixe')
brace(ax, 4, 84, 27, 'fixe', label='16 éléments = 8 paquets de 2')
text(ax, 44, 10, r'$1+1=0$ : paquet de $p=2$', 'resultat', 's')
save(fig, '67-037')
