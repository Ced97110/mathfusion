import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(52)
cx, cy, u = 14, 14, 9
for i in range(0, 4):
    for j in range(0, 3):
        disc(ax, cx + i*u, cy + j*u, 0.5, 'fixe')
P = lambda a, b: (cx + a*u, cy + b*u)
ax.add_patch(Arc((cx, cy), 2*u, 2*u, theta1=0, theta2=78, ec=COL['sujet'], lw=1.1, zorder=3))
arrow(ax, (cx + u*math.cos(math.radians(70)), cy + u*math.sin(math.radians(70))), (cx, cy + u), 'sujet')
arrow(ax, (cx + 1.6, cy + u), P(3, 1), 'varie', lw=1.4)
disc(ax, *P(0, 0), 0.9, 'encre')
disc(ax, *P(1, 0), 1.3, 'fixe'); disc(ax, *P(0, 1), 1.3, 'sujet'); disc(ax, *P(3, 1), 1.3, 'resultat')
text(ax, P(1, 0)[0] + 2.5, P(1, 0)[1] - 3.5, r'$x$', 'fixe', 's')
text(ax, P(0, 1)[0] - 2.5, P(0, 1)[1] + 3.5, r'$Ax$', 'sujet', 's')
text(ax, P(3, 1)[0], P(3, 1)[1] + 4, r'$Ax+b$', 'resultat', 's')
text(ax, 21, 38, r'$f(x)=Ax+b$', 'encre', 'l', ha='left')
text(ax, 21, 5, 'A : le quart de tour', 'sujet', 's', ha='left')
text(ax, 60, 5, 'b : glisse de 3', 'varie', 's', ha='left')
save(fig, '74-090')
