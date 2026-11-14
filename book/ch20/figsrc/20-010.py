import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mkP(ox, oy, sx, sy): return lambda x, y: (ox + sx * x, oy + sy * y)
def axes(ax, P, x0, x1, y0, y1, lx='$x$', ly='$y$'):
    arrow(ax, P(x0, 0), P(x1, 0), 'fixe', lw=0.7); arrow(ax, P(0, y0), P(0, y1), 'fixe', lw=0.7)
    text(ax, P(x1, 0)[0] + 1.5, P(x1, 0)[1] - 2.8, lx, 'fixe', 's'); text(ax, P(0, y1)[0] + 3, P(0, y1)[1] + 1, ly, 'fixe', 's')
def hollow(ax, p, role='sujet', r=1.3):
    ax.add_patch(Circle(p, r, ec=COL[role], fc='white', lw=0.9, zorder=6))

fig, ax = canvas(64)
P = mkP(30, 16, 9, 9)
axes(ax, P, -2.2, 3.4, -1.2, 4.6)
line(ax, [P(-2, -1), P(3.2, 4.2)], 'sujet', lw=1.2, dash=True)
text(ax, 66, 60, r'$y>x+1$', 'sujet', 'l', weight='bold')
text(ax, *P(-1.8, 1.9), r'$y=x+1$', 'sujet', 's', ha='left')
disc(ax, *P(0, 3), 1.5, 'resultat'); disc(ax, *P(0, 0), 1.5, 'limite')
text(ax, P(0, 3)[0] - 3, P(0, 3)[1] + 2.2, '(0, 3)', 'resultat', 's', ha='right')
text(ax, P(0, 3)[0] - 3, P(0, 3)[1] - 2, r'$3>1$ : vrai', 'resultat', 's', ha='right')
text(ax, P(0, 0)[0] + 3, P(0, 0)[1] + 4.2, '(0, 0)', 'limite', 's', ha='left')
text(ax, P(0, 0)[0] + 3, P(0, 0)[1] + 0.2 - 4, r'$0>1$ : faux', 'limite', 's', ha='left')
save(fig, '20-010')
