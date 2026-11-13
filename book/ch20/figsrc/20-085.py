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
fig, ax = canvas(88)
P = mk(14, 28, 7); win = (-1, 7, -3, 8)
frame(ax, P, win)
shade(ax, P, 2, 7, -3, 8)
vline(ax, P, 2, -3, 8)
text(ax, *P(2, -0.8), '2', 'sujet', 's', ha='right')
for (x, y) in ((3, -2), (5, 0)): dot(ax, P, x, y, 'resultat', 1.5)
text(ax, *P(3.3, -2), r'$(3,-2)$', 'resultat', 's', ha='left')
text(ax, *P(5, 0.9), r'$(5,0)$', 'resultat', 's')
arrow(ax, P(3, 4.6), P(3, 7.2), 'resultat')
text(ax, *P(3.3, 6.0), r'$(3,100)$', 'resultat', 's', ha='left')
dot(ax, P, 2, 6, 'limite', 1.5)
text(ax, *P(1.7, 6), r'$(2,7)$', 'limite', 's', ha='right')
save(fig, '20-085')
