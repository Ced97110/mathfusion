import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mkP(ox, oy, sx, sy): return lambda x, y: (ox + sx * x, oy + sy * y)
def axes(ax, P, x0, x1, y0, y1, lx='$x$', ly='$y$'):
    arrow(ax, P(x0, 0), P(x1, 0), 'fixe', lw=0.7); arrow(ax, P(0, y0), P(0, y1), 'fixe', lw=0.7)
    text(ax, P(x1, 0)[0] + 1.5, P(x1, 0)[1] - 2.8, lx, 'fixe', 's'); text(ax, P(0, y1)[0] + 3, P(0, y1)[1] + 1, ly, 'fixe', 's')
def hollow(ax, p, role='sujet', r=1.3):
    ax.add_patch(Circle(p, r, ec=COL[role], fc='white', lw=0.9, zorder=6))

fig, ax = canvas(76)
text(ax, 36, 71, 'point vide : 2 exclu', 'sujet', 's'); text(ax, 62, 71, r'$x>2$', 'sujet', 'm')
f = numberline(ax, 12, 60, 62, 0, 4, 1, True, 'fixe', True)
line(ax, [(f(2), 62), (65, 62)], 'sujet', lw=2.2)
hollow(ax, (f(2), 62), 'sujet', 1.5)
text(ax, 44, 49, 'même rôle : limite exclue', 'encre', 'm')
ax.add_patch(Polygon([(12, 6), (62, 38), (12, 38)], closed=True, ec='none', fc=FILL['sujet'], zorder=2))
line(ax, [(12, 6), (62, 38)], 'sujet', lw=1.2, dash=True)
for t in (0.15, 0.35, 0.55, 0.75, 0.95): hollow(ax, (12 + 50 * t, 6 + 32 * t), 'sujet', 1.3)
text(ax, 24, 31, r'$y>x+1$', 'sujet', 's')
text(ax, 64, 17, 'droite en pointillés :\npoints exclus', 'sujet', 's')
save(fig, '20-012')
