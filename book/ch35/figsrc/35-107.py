import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(70)
x0, k = 8, 0.4
X = lambda g: x0 + g * k
box(ax, X(0), 56, 50 * k, 9, 'sujet', label=r'$A$ 50°'); box(ax, X(50), 56, 70 * k, 9, 'autre', label=r'$B$ 70°'); box(ax, X(120), 56, 60 * k, 9, 'varie', label=r'$C$ 60°')
s = 150; a = 0.3265 * s
text(ax, 8, 46, 'fraction des sinus', 'sujet', 's', ha='left')
box(ax, 8, 34, a, 9, 'sujet', label='0,8397 / 2,5717 = 0,3265', size='s')
text(ax, 8, 26, r'$\tan25^\circ\times\tan35^\circ$ (moitiés de $A$ et $B$)', 'autre', 's', ha='left')
box(ax, 8, 14, a, 9, 'autre', label='0,3265')
line(ax, [(8 + a, 12), (8 + a, 45)], 'resultat', dash=True)
text(ax, 8 + a + 3, 29, '=', 'resultat', 'l', ha='left')
text(ax, 44, 5, 'les deux côtés valent 0,3265', 'resultat', 's')
save(fig, '35-107')
