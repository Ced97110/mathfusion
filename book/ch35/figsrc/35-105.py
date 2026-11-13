import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(62)
s = 80; x0 = 4
text(ax, x0, 55, r'$\sin25^\circ+\sin18^\circ$', 'encre', 'm', ha='left')
a, b = 0.4226 * s, 0.3090 * s
box(ax, x0, 40, a, 9, 'sujet', label='0,4226'); box(ax, x0 + a, 40, b, 9, 'autre', label='0,3090')
text(ax, 44, 33, '=', 'encre', 'l')
text(ax, x0, 26.5, r'$2\sin21{,}5^\circ\cos3{,}5^\circ$', 'encre', 'm', ha='left')
box(ax, x0, 11, a + b, 9, 'resultat', label='0,7316')
line(ax, [(x0 + a + b, 9), (x0 + a + b, 50)], 'fixe', dash=True)
text(ax, 44, 4, '25 et 18 → 21,5 et 3,5', 'fixe', 's')
save(fig, '35-105')
