import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(72)
xa, xb, yc, amp = 8, 80, 34, 14
text(ax, 44, 68, 'diapason 440, corde 442', 'fixe', 's')
text(ax, 44, 61, 'battements : 2 par seconde', 'resultat', 'm')
line(ax, [(xa, yc), (xb, yc)], 'fixe', lw=0.5)
wv(ax, lambda t: math.cos(2 * pi * t), xa, xb, yc, amp, 'fixe', 0, 1, dash=True)
wv(ax, lambda t: abs(math.cos(2 * pi * t)), xa, xb, yc, amp, 'sujet', 0, 1, lw=1.4)
f = numberline(ax, xa, xb, 18, 0, 1, 0.5, arrow_right=False)
text(ax, 85, 18, 's', 'fixe', 's')
for k, v in ((1, 0.5), (2, 1)):
    disc(ax, f(v), yc + amp, 1.3, 'resultat'); text(ax, f(v), yc + amp + 4, str(k), 'resultat', 's')
line(ax, [(8, 7), (14, 7)], 'fixe', dash=True); text(ax, 16, 7, 'cos : fréquence 1', 'fixe', 's', ha='left')
line(ax, [(52, 7), (58, 7)], 'sujet'); text(ax, 60, 7, 'volume', 'sujet', 's', ha='left')
save(fig, '35-101')
