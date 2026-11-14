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
fig, ax = canvas(64)
P = mk(16, 14, 9); win = (-1, 5, -1, 4.5)
frame(ax, P, win, lab=False)
text(ax, *P(4.7, -0.5), r'$x$', 'fixe', 's')
text(ax, *P(0.4, 4.1), r'$y$', 'fixe', 's')
shade(ax, P, -1, 5, 2, 4.5)
hline(ax, P, 2, -1, 5)
for h, r in ((3, 'resultat'), (1, 'limite')):
    hline(ax, P, h, 0, 3, r, dash=True, lw=0.7)
    dot(ax, P, 3, h, r, 1.5)
    text(ax, *P(0, h), f'{h}', r, 's', ha='right')
text(ax, *P(-0.2, 2), '2', 'sujet', 's', ha='right')
text(ax, *P(3.3, 3.0), 'plus haut que 2', 'resultat', 's', ha='left')
text(ax, *P(3.3, 1.0), 'plus bas', 'limite', 's', ha='left')
text(ax, *P(4.9, 2.0 + 0.0), r'$y=2$', 'sujet', 's', ha='right')
save(fig, '20-094')
