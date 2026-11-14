import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi
def arc(ax, c, r, a0, a1, role, n=60, dash=False, lw=1.0):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)

fig, ax = canvas(58)
ox, oy, u = 10, 12, 8
al = math.degrees(math.atan2(4, 3)); P = (ox + 3 * u, oy + 4 * u)
line(ax, [(ox, oy), (ox + 5 * u + 6, oy)], 'fixe', lw=0.8); line(ax, [(ox, oy), P], 'fixe', lw=0.8)
arc(ax, (ox, oy), 5 * u, 0, al, 'autre', dash=True, lw=1.3)
arrow(ax, (ox + u, oy + 5), (ox + 5 * u, oy + 5), 'varie', lw=1.3)
disc(ax, ox + u, oy, 1.5, 'sujet'); disc(ax, P[0], P[1], 1.5, 'resultat')
text(ax, ox + u, oy - 4, 'départ (1 ; 0)', 'sujet', 's')
text(ax, P[0], P[1] + 4, 'arrivée (3 ; 4)', 'resultat', 's')
text(ax, 84, 30, 'tourne de 53,13°', 'autre', 's', ha='right')
text(ax, ox + 3 * u + 4, oy + 9, '× 5', 'varie', 'm')
text(ax, 44, 54, r'multiplier par $3+4i$', 'encre', 'm')
save(fig, '35-111')
