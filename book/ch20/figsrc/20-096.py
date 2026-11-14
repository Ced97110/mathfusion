import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
plt.rcParams['hatch.linewidth'] = 0.45
IDP = lambda x, y: (x, y)
def mk(ox, oy, u): return lambda x, y: (ox + x * u, oy + y * u)
def shade(ax, P, x0, x1, y0, y1, role='resultat', hatch=True):
    ax.add_patch(Polygon([P(x0, y0), P(x1, y0), P(x1, y1), P(x0, y1)], closed=True, fc=FILL[role], ec=COL[role], lw=0, hatch='////' if hatch else None, zorder=1))
def frame(ax, P, win, lab=True):
    x0, x1, y0, y1 = win
    poly(ax, [P(x0, y0), P(x1, y0), P(x1, y1), P(x0, y1)], 'fixe', fill=False, lw=0.6)
    if x0 < 0 < x1: line(ax, [P(0, y0), P(0, y1)], 'fixe', lw=0.5)
    if y0 < 0 < y1: line(ax, [P(x0, 0), P(x1, 0)], 'fixe', lw=0.5)
    if lab:
        text(ax, *P(x1 - 0.3, -0.7), r'$x$', 'fixe', 's')
        text(ax, *P(0.6, y1 - 0.5), r'$y$', 'fixe', 's')
def dot(ax, P, x, y, role, r=1.3, fill=True):
    ax.add_patch(Circle(P(x, y), r, ec=COL[role], fc=FILL[role] if fill else 'white', lw=1.0, zorder=6))
def vline(ax, P, x, y0, y1, role='sujet', dash=True, lw=1.3): line(ax, [P(x, y0), P(x, y1)], role, lw=lw, dash=dash)
def hline(ax, P, y, x0, x1, role='sujet', dash=True, lw=1.3): line(ax, [P(x0, y), P(x1, y)], role, lw=lw, dash=dash)
fig, ax = canvas(72)
win = (-5, 3, -2, 7)
P1 = mk(46.0 - 4.2 * 8 - 3, 14, 4.2); P1 = mk(4 + 5 * 4.2, 20, 4.2); P2 = mk(48 + 5 * 4.2, 20, 4.2)
text(ax, 21, 66, r'$a=b=0$ : $0<5$', 'sujet', 'm')
text(ax, 65, 66, r'$a=0,\ b=1$ : $y<5$', 'autre', 'm')
frame(ax, P1, win, lab=False); frame(ax, P2, win, lab=False)
shade(ax, P1, -5, 3, -2, 7)
shade(ax, P2, -5, 3, -2, 5); hline(ax, P2, 5, -5, 3, 'autre')
for P, r2 in ((P1, 'resultat'), (P2, 'limite')):
    dot(ax, P, 1, 1, 'resultat', 1.5)
    text(ax, *P(1, 2.0), r'$(1,1)$', 'resultat', 's')
    arrow(ax, P(-4, 5.2), P(-4, 6.9), r2)
    text(ax, *P(-3.6, 6.3), r'$(-4,100)$', r2, 's', ha='left')
text(ax, 21, 6, 'tout le plan', 'resultat', 's')
text(ax, 65, 6, 'pas tout le plan', 'limite', 's')
save(fig, '20-096')
