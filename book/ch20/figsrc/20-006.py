import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mkP(ox, oy, sx, sy): return lambda x, y: (ox + sx * x, oy + sy * y)
def axes(ax, P, x0, x1, y0, y1, lx='$x$', ly='$y$'):
    arrow(ax, P(x0, 0), P(x1, 0), 'fixe', lw=0.7); arrow(ax, P(0, y0), P(0, y1), 'fixe', lw=0.7)
    text(ax, P(x1, 0)[0] + 1.5, P(x1, 0)[1] - 2.8, lx, 'fixe', 's'); text(ax, P(0, y1)[0] + 3, P(0, y1)[1] + 1, ly, 'fixe', 's')
def hollow(ax, p, role='sujet', r=1.3):
    ax.add_patch(Circle(p, r, ec=COL[role], fc='white', lw=0.9, zorder=6))

fig, ax = canvas(66)
P = mkP(14, 10, 10, 10)
axes(ax, P, -0.2, 6.9, -0.2, 4.7)
line(ax, [P(6, 0), P(0, 4)], 'fixe', lw=0.8, dash=True)
line(ax, [P(3, 2), P(6, 2), P(6, 0)], 'varie', lw=1.1); line(ax, [P(0, 4), P(3, 4), P(3, 2)], 'varie', lw=1.1)
text(ax, *P(4.5, 2.5), r'$-3$', 'varie', 'm'); text(ax, P(6, 1)[0] + 4, P(6, 1)[1], r'$+2$', 'varie', 'm')
text(ax, *P(1.5, 4.5), r'$-3$', 'varie', 'm'); text(ax, P(3, 3)[0] + 4, P(3, 3)[1], r'$+2$', 'varie', 'm')
for (a, b) in [(6, 0), (3, 2), (0, 4)]: disc(ax, *P(a, b), 1.6, 'resultat')
text(ax, P(6, 0)[0] + 1, P(6, 0)[1] - 4.5, '(6, 0)', 'resultat', 's')
text(ax, P(3, 2)[0] - 3, P(3, 2)[1] - 4, '(3, 2)', 'resultat', 's')
text(ax, P(0, 4)[0] + 3, P(0, 4)[1] - 4.5, '(0, 4)', 'resultat', 's', ha='left')
save(fig, '20-006')
