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
dot(ax, IDP, f(3), 72, 'varie', 1.6)
text(ax, f(3), 77, '3', 'varie', 'm')
P = mk(10, 28, 12); win = (-0.5, 5.5, -1.5, 1.5)
text(ax, 4, 52, 'dans le plan', 'encre', 'm', ha='left')
frame(ax, P, win)
shade(ax, P, 2, 5.5, -1.5, 1.5, hatch=False)
for i in range(1, 15): vline(ax, P, 2 + 0.25 * i, -1.5, 1.5, 'resultat', dash=False, lw=0.5)
vline(ax, P, 2, -1.5, 1.5)
vline(ax, P, 3, -1.5, 1.5, 'varie', dash=False, lw=1.8)
arrow(ax, (f(3), 69.5), (f(3), 47), 'varie')
text(ax, f(3) + 3, 59, 'tous les couples $(3,y)$', 'varie', 's', ha='left')
save(fig, '20-090')
