import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(100)
xa, xb = 8, 80
text(ax, 8, 95, 'diapason : 440', 'sujet', 's', ha='left')
wv(ax, lambda t: math.sin(t), xa, xb, 85, 6, 'sujet', 0, 16 * pi, n=600, lw=0.9)
text(ax, 8, 75, 'corde juste : 440', 'autre', 's', ha='left')
wv(ax, lambda t: math.sin(t), xa, xb, 65, 6, 'autre', 0, 16 * pi, n=600, lw=0.9)
text(ax, 44, 74.5, '+', 'encre', 'l'); text(ax, 44, 52, '=', 'encre', 'l')
text(ax, 8, 47, 'somme : deux fois plus haute', 'resultat', 's', ha='left')
wv(ax, lambda t: 2 * math.sin(t), xa, xb, 30, 6, 'resultat', 0, 16 * pi, n=600, lw=1.1)
line(ax, [(xa, 42), (xb, 42)], 'resultat', dash=True, lw=0.7); line(ax, [(xa, 18), (xb, 18)], 'resultat', dash=True, lw=0.7)
text(ax, 44, 9, 'volume constant', 'resultat', 'm')
save(fig, '35-102')
