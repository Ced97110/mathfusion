import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
from matplotlib.patches import Circle

fig, ax = canvas(72)

def point(x, y, r, role):
    ax.add_patch(Circle((x, y), r, fc=COL[role], ec='none', zorder=3))

# Nombre 35 coupé en dizaines et en unités
text(ax, 44, 68, '35 = 3 dizaines + 5', 'encre', 'm')

# Trois dizaines : 10 points chacune, rangés en deux paquets de 5 entourés de vert
for x0 in (4, 23, 42):
    box(ax, x0, 50, 18, 12, 'fixe')
    for y in (57.5, 52.5):
        for i in range(5):
            point(x0 + 3 + 3 * i, y, 0.9, 'fixe')
        box(ax, x0 + 1.5, y - 1.6, 15, 3.2, 'resultat', fill=False, dash=True, r=0.3)
brace(ax, 4, 60, 48, 'fixe', label=r'chaque dizaine = 5 $\times$ 2', down=True, size='s')

# Unités : 5 points orange, un seul paquet de 5 entouré de vert
box(ax, 66, 50, 18, 12, 'varie')
for x in (69, 72, 75, 78, 81):
    point(x, 56, 0.9, 'varie')
box(ax, 67.5, 54.4, 15, 3.2, 'resultat', fill=False, dash=True, r=0.3)
arrow(ax, (75, 50), (48.5, 35), 'varie')

# Rangée des dix chiffres : 0 et 5 verts, 6 rouge, les autres gris
for i in range(10):
    role = 'resultat' if i in (0, 5) else ('limite' if i == 6 else 'fixe')
    box(ax, 4 + 8 * i, 24, 7.4, 9, role, label=str(i), size='l')

# Verdicts sous la rangée
text(ax, 47.7, 19, '35', 'resultat', 's')
text(ax, 55.7, 19, '2 346', 'limite', 's')

save(fig, '03-091')
