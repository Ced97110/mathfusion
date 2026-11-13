import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(68)
ax.add_patch(Ellipse((44, 44), 80, 28, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=1))
for x, s in [(18, '(2, 3)'), (44, '(4, 6)'), (70, '(6, 9)')]:
    text(ax, x, 46, s, 'sujet', 'm')
text(ax, 44, 36, 'les couples qui vont ensemble…', 'sujet', 's')
arrow(ax, (44, 29), (44, 19), 'varie')
box(ax, 24, 4, 40, 14, 'resultat', label=r'fraction $\frac{2}{3}$', size='l')
text(ax, 44, 61, 'un groupe entier', 'sujet', 's')
save(fig, '54-040')
