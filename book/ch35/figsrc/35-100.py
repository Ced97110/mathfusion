import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(74)
xa, xb, yc, amp = 8, 80, 42, 14
text(ax, 44, 70, r'$2\sin(2\pi\times441\,t)\cos(2\pi\times1\,t)$', 'encre', 'm')
line(ax, [(8, 62), (14, 62)], 'sujet'); text(ax, 16, 62, 'note : 441', 'sujet', 's', ha='left')
line(ax, [(46, 62), (52, 62)], 'varie', dash=True); text(ax, 54, 62, 'rythme lent : 1', 'varie', 's', ha='left')
line(ax, [(xa, yc), (xb, yc)], 'fixe', lw=0.5)
env = lambda t: abs(math.cos(2 * pi * t))
wv(ax, env, xa, xb, yc, amp, 'varie', 0, 1, dash=True, lw=1.0)
wv(ax, lambda t: -env(t), xa, xb, yc, amp, 'varie', 0, 1, dash=True, lw=1.0)
wv(ax, lambda t: math.cos(2 * pi * t) * math.sin(2 * pi * 24 * t), xa, xb, yc, amp, 'sujet', 0, 1, n=1200, lw=0.7)
f = numberline(ax, xa, xb, 22, 0, 1, 0.5, arrow_right=False)
text(ax, 85, 22, 's', 'fixe', 's')
for v in (0, 0.5, 1): disc(ax, f(v), yc + amp, 1.2, 'resultat')
text(ax, 44, 12, 'volume maximal : 0 ; 0,5 ; 1', 'resultat', 's')
save(fig, '35-100')
