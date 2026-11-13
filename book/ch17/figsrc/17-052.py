import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 28
f = numberline(ax, 8, 70, y, 0, 4, arrow_right=False)
arrow(ax, (f(2) + 1.8, y), (80, y), 'fixe', lw=2.2)
ax.add_patch(Circle((f(2), y), 2.0, ec=COL['sujet'], fc=FILL['encre'], lw=1.5, zorder=3))
text(ax, 44, 51, r'$x > 2$', 'fixe', 'l')
text(ax, f(2), 40, 'remplissage : vide', 'sujet', 'm', weight='bold')
text(ax, f(2), 35.5, 'le bord est exclu', 'sujet', 's')
line(ax, [(f(2), 33.5), (f(2), 30.5)], 'sujet')
text(ax, 66, 33, 'flèche : le côté', 'fixe', 's')
text(ax, f(2), 14, 'place : le bord', 'fixe', 's')
text(ax, 44, 5, 'trois éléments, un seul est ici', 'fixe', 's')
save(fig, '17-052')
