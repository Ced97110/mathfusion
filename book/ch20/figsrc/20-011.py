import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mkP(ox, oy, sx, sy): return lambda x, y: (ox + sx * x, oy + sy * y)
def axes(ax, P, x0, x1, y0, y1, lx='$x$', ly='$y$'):
    arrow(ax, P(x0, 0), P(x1, 0), 'fixe', lw=0.7); arrow(ax, P(0, y0), P(0, y1), 'fixe', lw=0.7)
    text(ax, P(x1, 0)[0] + 1.5, P(x1, 0)[1] - 2.8, lx, 'fixe', 's'); text(ax, P(0, y1)[0] + 3, P(0, y1)[1] + 1, ly, 'fixe', 's')
def hollow(ax, p, role='sujet', r=1.3):
    ax.add_patch(Circle(p, r, ec=COL[role], fc='white', lw=0.9, zorder=6))

fig, ax = canvas(76)
P = mkP(40, 24, 10, 10)
ax.add_patch(Polygon([P(-3, -2), P(3, 4), P(-3, 4)], closed=True, ec='none', fc=FILL['sujet'], zorder=2))
line(ax, [P(-3, -2), P(3, 4)], 'sujet', lw=1.2, dash=True)
axes(ax, P, -3.3, 3.3, -2.3, 4.5)
disc(ax, *P(-1, 2), 1.5, 'resultat'); disc(ax, *P(0, 0), 1.5, 'limite')
text(ax, P(-1, 2)[0] - 2.5, P(-1, 2)[1] - 0.5, r'$A(-1,\,2)$', 'resultat', 's', ha='right')
text(ax, P(0, 0)[0] + 2.5, P(0, 0)[1] - 3, r'$O(0,\,0)$', 'limite', 's', ha='left')
text(ax, *P(-1.7, 3.4), r'zone $y>x+1$', 'sujet', 's')
text(ax, P(2.3, 2.4)[0], P(2.3, 2.4)[1], 'pointillés', 'sujet', 's', ha='left')
save(fig, '20-011')
