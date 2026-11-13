import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(56)
# écriture découpée à gauche
y = 38; xg, xa, xc = 8, 20, 32
text(ax, xg, y, 'G', 'fixe', 'xl'); text(ax, xa, y, 'A', 'sujet', 'xl'); text(ax, xc, y, 'C', 'fixe', 'xl')
line(ax, [(xa - 3, y + 5), (xa, y + 8), (xa + 3, y + 5)], 'varie', 1.2)
text(ax, xa, y + 13, 'chapeau : angle', 'varie', 's')
for x in (xg, xa, xc): line(ax, [(x, y - 5), (x, y - 9)], 'fixe', 0.7)
text(ax, xa, y - 12, 'sommet', 'sujet', 's')
text(ax, xg, y - 17, 'un point', 'fixe', 's'); text(ax, xc, y - 17, 'un point', 'fixe', 's')
text(ax, xa, y - 22, 'sur chaque côté', 'fixe', 's')
text(ax, xa, 6, r'même angle : $\alpha$', 'varie', 's')
# angle dessiné à droite
Ap = (50, 12); Cp = (84, 12); Gp = (80, 33)
line(ax, [Ap, Cp], 'fixe', 1.4); line(ax, [Ap, Gp], 'fixe', 1.4)
a = math.degrees(math.atan2(Gp[1] - Ap[1], Gp[0] - Ap[0]))
ax.add_patch(Arc(Ap, 20, 20, theta1=0, theta2=a, color=COL['varie'], lw=1.3, zorder=3))
disc(ax, *Ap, 1.1, 'sujet'); disc(ax, *Cp, 1.0, 'fixe'); disc(ax, *Gp, 1.0, 'fixe')
text(ax, Ap[0] - 1, Ap[1] - 4, 'A', 'sujet'); text(ax, Cp[0] - 1, Cp[1] - 4, 'C', 'fixe'); text(ax, Gp[0] - 1, Gp[1] + 4, 'G', 'fixe')
text(ax, 64, 15.5, r'$\alpha$', 'varie', 's')
save(fig, '27-042')
