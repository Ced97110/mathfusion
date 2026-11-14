import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, k = 26, 36
X = lambda v: ox + v * k
bh = 4.5
def bar(y, segs, half=None):
    for (a, b, role, yy, hh) in segs:
        box(ax, X(a), yy, (b - a) * k, hh, role, r=0.5)
text(ax, 3, 79, '35°', 'encre', 'l', ha='left', weight='bold')
text(ax, 3, 46, '120°', 'encre', 'l', ha='left', weight='bold')
# 35 deg, sans carres
text(ax, 3, 72, r'$\sin\theta+\cos\theta=1{,}3928$', 'limite', 's', ha='left')
bar(0, [(0, 0.5736, 'varie', 64.5, bh), (0.5736, 1.3928, 'autre', 64.5, bh)])
text(ax, 3, 59, r'$\sin^2\theta+\cos^2\theta=1$', 'resultat', 's', ha='left')
bar(0, [(0, 0.3290, 'varie', 52, bh), (0.3290, 1.0, 'autre', 52, bh)])
# 120 deg
text(ax, 3, 39, r'$\sin\theta+\cos\theta=0{,}3660$', 'limite', 's', ha='left')
bar(0, [(-0.5, 0.366, 'varie', 33.5, 2.4), (-0.5, 0, 'autre', 31, 2.4)])
text(ax, 3, 26, r'$\sin^2\theta+\cos^2\theta=1$', 'resultat', 's', ha='left')
bar(0, [(0, 0.75, 'varie', 18.5, bh), (0.75, 1.0, 'autre', 18.5, bh)])
line(ax, [(X(1), 14), (X(1), 77)], 'resultat', dash=True)
text(ax, X(1) + 3, 79, '1', 'resultat', 'm', weight='bold')
line(ax, [(X(0), 14), (X(0), 77)], 'fixe')
box(ax, 20, 4, 8, 4.5, 'varie', r=0.5); text(ax, 31, 6.3, 'sin', 'varie', 's', ha='left')
box(ax, 46, 4, 8, 4.5, 'autre', r=0.5); text(ax, 57, 6.3, 'cos', 'autre', 's', ha='left')
save(fig, '31-072')
