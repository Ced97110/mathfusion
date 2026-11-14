import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def shrink(p, q, d):
    n = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / n, (q[1] - p[1]) / n)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
xb, xa, r = 36, 64, 3.8
ys = {'A': 46, 'B': 30, 'C': 14}
for k, y in ys.items():
    disc(ax, xb, y, r, 'sujet', label=r'$P_%s$' % k, size='s'); disc(ax, xa, y, r, 'sujet', label=r'$P_%s$' % k, size='s')
for a, b in (('A', 'A'), ('B', 'C'), ('C', 'B')):
    p, q = shrink((xb, ys[a]), (xa, ys[b]), r + 0.8); arrow(ax, p, q, 'varie', lw=1.2)
text(ax, 50, 57, r'$s_A$ agit', 'varie', 's')
box(ax, 28.5, 39.5, 15, 13, 'resultat', fill=False, dash=True)
box(ax, 28.5, 8, 15, 29, 'resultat', fill=False, dash=True)
text(ax, 14, 46, 'taille 1', 'resultat', 's'); text(ax, 14, 22, 'taille 2', 'resultat', 's')
text(ax, 79, 30, r'$1+2=3$', 'resultat', 's')
text(ax, 50, 3, r'$e$ ne bouge rien', 'fixe', 's')
save(fig, '50-096')
