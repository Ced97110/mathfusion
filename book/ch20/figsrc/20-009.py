import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mkP(ox, oy, sx, sy): return lambda x, y: (ox + sx * x, oy + sy * y)
def axes(ax, P, x0, x1, y0, y1, lx='$x$', ly='$y$'):
    arrow(ax, P(x0, 0), P(x1, 0), 'fixe', lw=0.7); arrow(ax, P(0, y0), P(0, y1), 'fixe', lw=0.7)
    text(ax, P(x1, 0)[0] + 1.5, P(x1, 0)[1] - 2.8, lx, 'fixe', 's'); text(ax, P(0, y1)[0] + 3, P(0, y1)[1] + 1, ly, 'fixe', 's')
def hollow(ax, p, role='sujet', r=1.3):
    ax.add_patch(Circle(p, r, ec=COL[role], fc='white', lw=0.9, zorder=6))

fig, ax = canvas(66)
P = mkP(14, 10, 8, 8)
poly(ax, [P(0, 0), P(6, 0), P(0, 4)], 'sujet')
line(ax, [P(6, 0), P(0, 4)], 'sujet', lw=1.4)
axes(ax, P, -0.2, 6.8, -0.4, 4.9)
for (a, b) in [(3, 2), (1, 1), (0, 0)]: disc(ax, *P(a, b), 1.5, 'resultat')
text(ax, P(3, 2)[0] + 2.5, P(3, 2)[1] + 3, '(3, 2)', 'resultat', 's', ha='left')
text(ax, P(1, 1)[0] + 2.5, P(1, 1)[1] + 2.5, '(1, 1)', 'resultat', 's', ha='left')
text(ax, P(0, 0)[0] + 2.5, P(0, 0)[1] - 3, '(0, 0)', 'resultat', 's', ha='left')
text(ax, *P(1.1, 2.6), 'région', 'sujet', 'm')
text(ax, P(4.8, 1.2)[0], P(4.8, 1.2)[1] + 1, 'droite', 'sujet', 's')
save(fig, '20-009')
