import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(62)
xa, xb, yb, amp = 12, 76, 18, 13
xm = (xa + xb) / 2
line(ax, [(xa - 4, yb), (xb + 4, yb)], 'fixe', lw=0.6)
wv(ax, lambda t: abs(2 * math.cos(t / 2)), xa, xb, yb, amp, 'sujet', 0, 2 * pi)
for x, r in ((xa, 'resultat'), (xm, 'autre'), (xb, 'resultat')): disc(ax, x, yb, 1.3, r)
disc(ax, xa, yb + 2 * amp, 1.3, 'resultat'); disc(ax, xb, yb + 2 * amp, 1.3, 'resultat')
text(ax, xa, yb + 2 * amp + 5, 'en phase : 2', 'resultat', 's'); text(ax, xb, yb + 2 * amp + 5, 'en phase : 2', 'resultat', 's')
text(ax, xm, yb + 2 * amp + 5, r'$|2\cos(x/2)|$', 'sujet', 'm')
for x, s in ((xa, '0'), (xm, r'$\pi$'), (xb, r'$2\pi$')): text(ax, x, yb - 4, s, 'fixe', 's')
text(ax, xm, yb - 9.5, 'en opposition : 0', 'autre', 's')
save(fig, '35-098')
