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
fig, ax = canvas(66)
win = (-1, 5, -1, 5)
P1 = mk(10, 14, 6); P2 = mk(56, 14, 6)
text(ax, 22, 58, r'$b=0$ : $x>2$', 'sujet', 'm')
text(ax, 68, 58, r'$a=0$ : $y>2$', 'autre', 'm')
frame(ax, P1, win); frame(ax, P2, win)
shade(ax, P1, 2, 5, -1, 5); vline(ax, P1, 2, -1, 5)
shade(ax, P2, -1, 5, 2, 5, 'resultat'); hline(ax, P2, 2, -1, 5, 'autre')
text(ax, *P1(1.8, -0.6), '2', 'sujet', 's', ha='right')
text(ax, *P2(-0.3, 1.5), '2', 'autre', 's', ha='right')
arrow(ax, (41.5, 38), (48.5, 38), 'varie', both=True)
text(ax, 44, 6, 'on échange $x$ et $y$', 'varie', 's')
save(fig, '20-092')
