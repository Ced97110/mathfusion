import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def pts(cx): return {'A': (cx, 40), 'B': (cx - 11, 20), 'C': (cx + 11, 20)}
def shrink(p, q, d):
    n = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / n, (q[1] - p[1]) / n)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
r = 3.9
for cx in (22, 66):
    for k, p in pts(cx).items(): disc(ax, p[0], p[1], r, 'sujet', label=r'$P_%s$' % k, size='s')
text(ax, 22, 58, r'sous $G$ : 1 orbite', 'encre', 's'); text(ax, 66, 58, r'sous $P_A$ : 2 orbites', 'encre', 's')
L = pts(22)
for a, b in (('A', 'B'), ('B', 'C'), ('C', 'A')):
    p, q = shrink(L[a], L[b], r + 0.8); arrow(ax, p, q, 'fixe', lw=1.1, curve=-0.25)
text(ax, 22, 28.5, r'$r$', 'fixe', 's')
box(ax, 4, 12, 36, 38, 'sujet', fill=False, dash=True)
text(ax, 22, 7, 'taille 3', 'sujet', 's')
R_ = pts(66)
box(ax, 59.5, 34, 13, 13, 'resultat', fill=False, dash=True)
box(ax, 48, 12.5, 36, 15, 'resultat', fill=False, dash=True)
p, q = shrink(R_['B'], R_['C'], r + 0.8); arrow(ax, p, q, 'sujet', lw=1.2, both=True)
text(ax, 66, 24, r'$s_A$', 'sujet', 's')
text(ax, 66, 7, 'tailles 1 et 2', 'resultat', 's')
save(fig, '50-092')
