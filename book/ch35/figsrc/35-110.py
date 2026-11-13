import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi
def arc(ax, c, r, a0, a1, role, n=60, dash=False, lw=1.0):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)

fig, ax = canvas(64)
ox, oy, u = 8, 10, 8
arrow(ax, (ox, oy), (ox + 3 * u, oy + 4 * u), 'sujet', lw=1.6)
arrow(ax, (ox, oy), (ox + 0.6 * u, oy + 0.8 * u), 'autre', lw=1.8)
text(ax, ox + 3 * u - 3, oy + 4 * u + 4, '(3 ; 4) : longueur 5', 'sujet', 's')
text(ax, ox + 6, oy + 5.5, '(0,6 ; 0,8) : longueur 1', 'autre', 's', ha='left')
text(ax, 44, 4.5, 'alignées : produit maximal', 'fixe', 's')
text(ax, 62, 56, r'$a\sin x+b\cos x$', 'encre', 'm')
text(ax, 62, 51, 'produits de même rang', 'fixe', 's')
text(ax, 62, 44, '3 × 0,6 = 1,8', 'fixe', 'm')
text(ax, 62, 36.5, '4 × 0,8 = 3,2', 'fixe', 'm')
text(ax, 62, 28, '1,8 + 3,2 = 5', 'resultat', 'm', weight='bold')
text(ax, 62, 20, '5 × 1 = 5', 'resultat', 'm')
save(fig, '35-110')
