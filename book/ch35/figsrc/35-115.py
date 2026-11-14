import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi
def arc(ax, c, r, a0, a1, role, n=60, dash=False, lw=1.0):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)

fig, ax = canvas(66)
u = 4; ox, oy = 30, 24
O = (ox, oy); A = (ox + 3 * u, oy); P = (ox + 3 * u, oy + 4 * u)
poly(ax, [O, A, (A[0], oy - 3 * u), (ox, oy - 3 * u)], 'sujet')
poly(ax, [A, P, (P[0] + 4 * u, P[1]), (A[0] + 4 * u, A[1])], 'autre')
poly(ax, [O, P, (P[0] - 4 * u, P[1] + 3 * u), (O[0] - 4 * u, O[1] + 3 * u)], 'resultat')
poly(ax, [O, A, P], 'encre', fill=True)
text(ax, ox + 1.5 * u, oy - 1.5 * u, r'$3^2=9$', 'sujet', 's')
text(ax, A[0] + 2 * u, A[1] + 2 * u, r'$4^2=16$', 'autre', 's')
text(ax, (O[0] + P[0]) / 2 - 2 * u - 1, (O[1] + P[1]) / 2 + 1.5 * u, r'$5^2=25$', 'resultat', 's')
text(ax, 44, 62, r'norme de $3+4i$ : $a^2+b^2=R^2$', 'encre', 's')
text(ax, 44, 4, '9 + 16 = 25', 'resultat', 'l')
save(fig, '35-115')
