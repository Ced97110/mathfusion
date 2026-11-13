import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi
def arc(ax, c, r, a0, a1, role, n=60, dash=False, lw=1.0):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)

fig, ax = canvas(72)
ox, oy, u = 30, 14, 8
al = math.degrees(math.atan2(4, 3))
P = (ox + 3 * u, oy + 4 * u)
arrow(ax, (ox - 2, oy), (ox + 36, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy - 2), (ox, oy + 46), 'fixe', lw=0.7)
line(ax, [(ox, oy), (P[0], oy), P], 'fixe', dash=True, lw=0.9)
line(ax, [(ox, oy), P], 'varie', lw=1.6)
arc(ax, (ox, oy), 9, 0, al, 'autre', lw=1.4)
disc(ax, P[0], P[1], 1.5, 'sujet')
text(ax, P[0] + 3, P[1] + 3, '(3 ; 4)', 'sujet', 'm', ha='left')
text(ax, ox + 1.5 * u, oy - 3.5, 'a = 3', 'fixe', 's'); text(ax, P[0] + 2, oy + 2 * u, 'b = 4', 'fixe', 's', ha='left')
text(ax, ox + 1.5 * u - 3, oy + 2 * u + 2, 'R = 5', 'varie', 's', ha='right')
text(ax, 84, 62, 'module R : distance', 'varie', 's', ha='right')
text(ax, 84, 55.5, 'argument α : angle', 'autre', 's', ha='right')
text(ax, ox + 11, oy + 3, '53,13°', 'autre', 's', ha='left')
text(ax, 4, 66, 'côtés (a ; b)  →  (R ; α)', 'encre', 'm', ha='left')
save(fig, '35-109')
