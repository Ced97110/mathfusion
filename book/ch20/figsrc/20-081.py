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
fig, ax = canvas(90)
text(ax, 4, 85, 'sur la droite des nombres', 'encre', 'm', ha='left')
f = numberline(ax, 10, 70, 72, 0, 5, labels=False)
arrow(ax, (f(2), 72), (78, 72), 'resultat', lw=2.2)
dot(ax, IDP, f(2), 72, 'sujet', 1.5, fill=False)
text(ax, f(2), 67, '2', 'sujet', 'm')
text(ax, 58, 78, 'demi-droite', 'resultat', 's')
text(ax, 4, 56, 'dans le plan', 'encre', 'm', ha='left')
P = mk(10, 28, 12); win = (-0.5, 5.5, -1.5, 1.5)
frame(ax, P, win)
shade(ax, P, 2, 5.5, -1.5, 1.5)
vline(ax, P, 2, -1.5, 1.5)
text(ax, *P(1.85, -1.1), '2', 'sujet', 'm', ha='right')
text(ax, 58, 50, 'demi-plan', 'resultat', 's')
save(fig, '20-081')
