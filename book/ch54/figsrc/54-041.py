import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(72)
ax.add_patch(Ellipse((24, 36), 44, 50, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=1))
text(ax, 24, 69, 'un seul groupe', 'sujet', 's')
text(ax, 70, 69, 'plusieurs noms', 'varie', 's')
for y, c, n in [(52, '(2, 3)', r'$\frac{2}{3}$'), (36, '(4, 6)', r'$\frac{4}{6}$'), (20, '(6, 9)', r'$\frac{6}{9}$')]:
    text(ax, 24, y, c, 'sujet', 'm')
    arrow(ax, (38, y), (56, y), 'varie')
    box(ax, 58, y - 6, 24, 12, 'varie', label=n, size='l')
text(ax, 24, 8, '… et tous les autres', 'sujet', 's')
text(ax, 70, 8, 'même groupe', 'resultat', 's')
save(fig, '54-041')
