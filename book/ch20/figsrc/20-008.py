import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mkP(ox, oy, sx, sy): return lambda x, y: (ox + sx * x, oy + sy * y)
def axes(ax, P, x0, x1, y0, y1, lx='$x$', ly='$y$'):
    arrow(ax, P(x0, 0), P(x1, 0), 'fixe', lw=0.7); arrow(ax, P(0, y0), P(0, y1), 'fixe', lw=0.7)
    text(ax, P(x1, 0)[0] + 1.5, P(x1, 0)[1] - 2.8, lx, 'fixe', 's'); text(ax, P(0, y1)[0] + 3, P(0, y1)[1] + 1, ly, 'fixe', 's')
def hollow(ax, p, role='sujet', r=1.3):
    ax.add_patch(Circle(p, r, ec=COL[role], fc='white', lw=0.9, zorder=6))

fig, ax = canvas(68)
P = mkP(12, 8, 18, 8)
axes(ax, P, -0.2, 3.3, -0.2, 6.5)
line(ax, [P(-0.1, 0.8), P(2.55, 6.1)], 'sujet', lw=1.4)
for i in range(1, 12):
    xv = 0.2 * i
    ax.add_patch(Circle(P(xv, 2 * xv + 1), 0.6, ec=COL['sujet'], fc=COL['sujet'], zorder=3))
for (a, b) in [(0, 1), (1, 3), (2, 5)]:
    disc(ax, *P(a, b), 1.6, 'sujet')
    text(ax, P(a, b)[0] + 3, P(a, b)[1] - 2.5, f'({a}, {b})', 'sujet', 's', ha='left')
text(ax, 56, 28, r'$y=2x+1$', 'sujet', 'm')
save(fig, '20-008')
