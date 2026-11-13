import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(88)
box(ax, 14, 70, 60, 14, 'sujet', label=r'$\sin\theta-\sin3\theta=0$', size='l')
text(ax, 44, 65, 'deux angles : θ et 3θ', 'sujet', 's')
arrow(ax, (44, 62), (44, 52), 'varie'); text(ax, 52, 57, 'factoriser', 'varie', 's', ha='left')
box(ax, 6, 36, 34, 12, 'autre', label=r'$-2\cos2\theta$', size='m')
text(ax, 44, 42, '×', 'encre', 'l')
box(ax, 48, 36, 34, 12, 'autre', label=r'$\sin\theta$', size='m')
text(ax, 23, 31, 'un angle : 2θ', 'autre', 's'); text(ax, 65, 31, 'un angle : θ', 'autre', 's')
text(ax, 44, 24, 'produit nul : l’un des deux est nul', 'fixe', 's')
arrow(ax, (23, 22.5 - 1), (23, 16), 'varie'); arrow(ax, (65, 22.5 - 1), (65, 16), 'varie')
box(ax, 6, 3, 34, 12, 'resultat', label=r'$\cos2\theta=0$', size='m')
box(ax, 48, 3, 34, 12, 'resultat', label=r'$\sin\theta=0$', size='m')
save(fig, '35-104')
