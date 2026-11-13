import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(66)
x0, k = 8, 0.4
X = lambda g: x0 + g * k
box(ax, X(0), 34, 50 * k, 9, 'sujet', label=r'$A$ 50°'); box(ax, X(50), 34, 70 * k, 9, 'autre', label=r'$B$ 70°'); box(ax, X(120), 34, 60 * k, 9, 'varie', label=r'$C$ 60°')
brace(ax, X(0), X(120), 46, 'fixe', r'$A+B=120^\circ$', down=False)
line(ax, [(X(90), 31), (X(90), 45)], 'fixe', dash=True)
disc(ax, X(60), 34, 1.3, 'resultat')
for g, s_ in ((0, '0°'), (90, '90°'), (180, '180°')): text(ax, X(g), 28.5, s_, 'fixe', 's')
text(ax, X(60), 28.5, '60°', 'resultat', 's')
arrow(ax, (X(90), 22), (X(60), 22), 'varie'); text(ax, X(75), 17, r'$C/2=30^\circ$', 'varie', 's')
text(ax, 44, 7, r'$(A+B)/2=60^\circ=90^\circ-30^\circ$', 'resultat', 'm')
save(fig, '35-106')
