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
fig, ax = canvas(80)
box(ax, 2, 64, 26, 9, 'sujet', label=r'$1\times x$')
text(ax, 33, 68.5, r'$+$')
box(ax, 38, 64, 26, 9, 'varie', label=r'$0\times y$')
text(ax, 72, 68.5, r'$>\ 2$')
arrow(ax, (44, 63), (44, 57), 'varie')
text(ax, 50, 60, r'$y$ a disparu', 'varie', 's', ha='left')
box(ax, 28, 46, 32, 9, 'resultat', label=r'$x>2$')
P = mk(14, 18, 8); win = (-1, 6, -2, 2)
frame(ax, P, win)
shade(ax, P, 2, 6, -2, 2)
vline(ax, P, 2, -2, 2)
arrow(ax, P(4, -1.5), P(4, 1.5), 'varie', both=True)
text(ax, *P(4.3, 0), r'$y$ libre', 'varie', 's', ha='left')
save(fig, '20-082')
