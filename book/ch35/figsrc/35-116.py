import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi
def arc(ax, c, r, a0, a1, role, n=60, dash=False, lw=1.0):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)

fig, ax = canvas(72)
cx, cy, R = 30, 34, 26
al = math.degrees(math.atan2(0.8, 0.6))
arc(ax, (cx, cy), R, 0, 360, 'fixe', n=120, dash=True, lw=0.7)
P0 = (cx + R, cy); P1 = (cx + 0.6 * R, cy + 0.8 * R)
line(ax, [(cx, cy), P0], 'sujet', lw=1.4); line(ax, [(cx, cy), P1], 'resultat', lw=1.4)
arc(ax, (cx, cy), 12, 0, al, 'varie', lw=1.6)
disc(ax, P0[0], P0[1], 1.5, 'sujet'); disc(ax, P1[0], P1[1], 1.5, 'resultat')
text(ax, P0[0] + 3, P0[1] - 3.5, '(1 ; 0)', 'sujet', 's', ha='left')
text(ax, P1[0] + 3, P1[1] + 3, '(0,6 ; 0,8)', 'resultat', 's', ha='left')
text(ax, 74, 22, 'tourne de 53,13°', 'varie', 's')
text(ax, 74, 14, 'distance : 1 → 1', 'fixe', 's')
text(ax, 44, 68, r'multiplier par $0{,}6+0{,}8i$', 'encre', 'm')
save(fig, '35-116')
