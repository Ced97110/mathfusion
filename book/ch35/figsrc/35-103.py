import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(70)
xa, xb, yc, amp = 10, 78, 34, 14
f = numberline(ax, xa, xb, yc, -180, 180, 45, every=4, arrow_right=False)
d = math.radians
wv(ax, lambda t: math.sin(d(t)), xa, xb, yc, amp, 'sujet', -180, 180, lw=1.3)
wv(ax, lambda t: math.sin(3 * d(t)), xa, xb, yc, amp, 'autre', -180, 180, lw=1.3)
sols = [-180, -135, -45, 0, 45, 135, 180]
for k, s in enumerate(sols, 1):
    disc(ax, f(s), yc + amp * math.sin(d(s)), 1.3, 'resultat')
    text(ax, f(s), 53, str(k), 'resultat', 'm', weight='bold')
    line(ax, [(f(s), 50), (f(s), yc + amp * math.sin(d(s)) + 1.5)], 'resultat', dash=True, lw=0.4)
text(ax, 82, yc + 3, r'$\theta$', 'fixe', 's')
line(ax, [(8, 66), (14, 66)], 'sujet'); text(ax, 16, 66, r'$\sin\theta$', 'sujet', 's', ha='left')
line(ax, [(34, 66), (40, 66)], 'autre'); text(ax, 42, 66, r'$\sin3\theta$', 'autre', 's', ha='left')
text(ax, 44, 8, 'sept points communs', 'resultat', 'm')
save(fig, '35-103')
