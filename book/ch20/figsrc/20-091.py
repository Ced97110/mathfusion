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
box(ax, 29, 78, 30, 9, 'sujet', label=r'$x>2$')
arrow(ax, (36, 77), (22, 62), 'varie'); arrow(ax, (52, 77), (66, 62), 'varie')
text(ax, 44, 68, 'où la lit-on ?', 'varie', 's')
text(ax, 22, 56, 'sur la droite', 'encre', 'm')
text(ax, 66, 56, 'dans le plan', 'encre', 'm')
f = numberline(ax, 4, 34, 38, 0, 5, labels=False)
dot(ax, IDP, f(3), 38, 'resultat', 1.6)
text(ax, f(3), 33, '3', 'resultat', 'm')
P = mk(50, 30, 5.5); win = (-0.5, 5.5, -3, 3)
frame(ax, P, win)
dot(ax, P, 3, -2, 'resultat', 1.6)
text(ax, *P(3.3, -2), r'$(3,-2)$', 'resultat', 's', ha='left')
text(ax, 22, 8, 'solutions : des nombres', 'resultat', 's')
text(ax, 66, 8, 'solutions : des couples', 'resultat', 's')
save(fig, '20-091')
