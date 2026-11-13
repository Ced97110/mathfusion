import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(80)
cx, cy = 44, 40
for a in (45, 135, 225, 315):
    ux, uy = math.cos(math.radians(a)), math.sin(math.radians(a))
    ax.add_patch(Ellipse((cx + 9 * ux, cy + 9 * uy), 31, 11, angle=a, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=1))
for a in (45, 135, 225, 315):
    ux, uy = math.cos(math.radians(a)), math.sin(math.radians(a))
    for d in (9, 18): disc(ax, cx + d * ux, cy + d * uy, 1.6, 'sujet')
disc(ax, cx, cy, 2.0, 'fixe')
text(ax, cx + 5.5, cy - 0.5, r'$e$', 'fixe', 'm')
text(ax, 44, 74, '4 sous-groupes de 3 éléments', 'sujet', 'm')
text(ax, 44, 66, r'chacun : $e$ et 2 autres', 'encre', 's')
text(ax, 44, 12, r'$4 \times 2 = 8$ éléments d’ordre 3', 'resultat', 'm')
text(ax, 44, 4, r'seul $e$ est commun', 'fixe', 's')
save(fig, '50-181')
