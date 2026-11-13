import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi
def arc(ax, c, r, a0, a1, role, n=60, dash=False, lw=1.0):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)

fig, ax = canvas(70)
xa, xb, yc, amp = 8, 80, 34, 14
al = math.radians(38.66); t0, t1 = -1.0, -1.0 + 2 * pi
fx = lambda t: xa + (t - t0) / (t1 - t0) * (xb - xa)
text(ax, 44, 65, r'$R\sin(x+\alpha)$', 'encre', 'l')
line(ax, [(xa, yc), (xb, yc)], 'fixe', lw=0.5)
wv(ax, lambda t: math.sin(t), xa, xb, yc, amp, 'fixe', t0, t1, dash=True)
wv(ax, lambda t: math.sin(t + al), xa, xb, yc, amp, 'sujet', t0, t1, lw=1.5)
tp = pi / 2 - al
line(ax, [(fx(tp), yc), (fx(tp), yc + amp)], 'resultat', lw=1.0)
disc(ax, fx(tp), yc + amp, 1.2, 'resultat')
text(ax, fx(tp) - 2, yc + 5, 'amplitude 6,403', 'resultat', 's', ha='right')
arrow(ax, (fx(pi / 2), yc + amp + 3), (fx(tp), yc + amp + 3), 'varie', lw=1.2)
text(ax, fx(tp) + 12, yc + amp + 7.5, 'déphasage 38,66°', 'varie', 's')
line(ax, [(8, 56), (14, 56)], 'fixe', dash=True); text(ax, 16, 56, r'$\sin x$', 'fixe', 's', ha='left')
text(ax, 66, 56, r'$5\sin x+4\cos x$', 'sujet', 's')
text(ax, 44, 8, 'deux nombres : R et α', 'sujet', 'm')
save(fig, '35-113')
