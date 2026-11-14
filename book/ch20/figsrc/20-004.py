import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mkP(ox, oy, sx, sy): return lambda x, y: (ox + sx * x, oy + sy * y)
def axes(ax, P, x0, x1, y0, y1, lx='$x$', ly='$y$'):
    arrow(ax, P(x0, 0), P(x1, 0), 'fixe', lw=0.7); arrow(ax, P(0, y0), P(0, y1), 'fixe', lw=0.7)
    text(ax, P(x1, 0)[0] + 1.5, P(x1, 0)[1] - 2.8, lx, 'fixe', 's'); text(ax, P(0, y1)[0] + 3, P(0, y1)[1] + 1, ly, 'fixe', 's')
def hollow(ax, p, role='sujet', r=1.3):
    ax.add_patch(Circle(p, r, ec=COL[role], fc='white', lw=0.9, zorder=6))

fig, ax = canvas(70)
P = mkP(14, 10, 8, 8)
poly(ax, [P(6, 0), P(6, 4), P(0, 4)], 'limite'); poly(ax, [P(0, 0), P(6, 0), P(0, 4)], 'resultat')
ax.add_patch(Rectangle(P(0, 0), 48, 32, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=2.5))
line(ax, [P(6, 0), P(0, 4)], 'sujet', lw=1.4)
axes(ax, P, -0.2, 6.8, -0.2, 4.9)
disc(ax, *P(6, 4), 1.3, 'limite')
text(ax, P(5.5, 3.3)[0], P(5.5, 3.3)[1], '(6, 4) : 24 €', 'limite', 's', ha='right')
text(ax, P(4.6, 2.2)[0], P(4.6, 2.2)[1], r'$2x+3y=12$', 'sujet', 's')
text(ax, P(1.5, 0.9)[0], P(1.5, 0.9)[1], 'permis', 'resultat', 's')
text(ax, P(6, 0)[0], P(6, 0)[1] - 5, r'pains $\leq6$', 'fixe', 's')
text(ax, P(0, 4)[0] + 1, P(0, 4)[1] + 4.5, r'gâteaux $\leq4$', 'fixe', 's', ha='left')
save(fig, '20-004')
