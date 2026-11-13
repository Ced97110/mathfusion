import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi
def arc(ax, c, r, a0, a1, role, n=60, dash=False, lw=1.0):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)

fig, ax = canvas(86)
cx, cy, R = 44, 48, 26
V = [(cx + R * math.cos(math.radians(72 * k)), cy + R * math.sin(math.radians(72 * k))) for k in range(5)]
poly(ax, V, 'fixe')
line(ax, [(cx - R, cy), (cx + R + 2, cy)], 'fixe', lw=0.6)
line(ax, [V[1], (V[1][0], cy)], 'sujet', dash=True); line(ax, [V[2], (V[2][0], cy)], 'autre', dash=True)
disc(ax, V[1][0], V[1][1], 1.2, 'sujet'); disc(ax, V[2][0], V[2][1], 1.2, 'autre')
text(ax, 86, V[1][1] + 6, r'$\cos72^\circ=0{,}3090$', 'sujet', 's', ha='right')
text(ax, 2, V[1][1] + 6, r'$\cos144^\circ=-0{,}8090$', 'autre', 's', ha='left')
f = numberline(ax, 18, 70, 12, -1, 1, 0.5, arrow_right=False)
arrow(ax, (f(0), 20), (f(0.309), 20), 'sujet', lw=1.3)
arrow(ax, (f(0.309), 25), (f(-0.5), 25), 'autre', lw=1.3)
line(ax, [(f(0.309), 20), (f(0.309), 25)], 'fixe', dash=True, lw=0.6)
disc(ax, f(-0.5), 12, 1.6, 'resultat')
text(ax, f(-0.5), 30, 'somme −0,5', 'resultat', 's')
save(fig, '35-112')
