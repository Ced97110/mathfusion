import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def short(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / L, (q[1] - p[1]) / L)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
box(ax, 3, 58, 36, 11, 'sujet', label=r'$H = \{0, 3, 6, 9\}$', size='s')
box(ax, 42, 58, 43, 11, 'autre', label=r'$K = \{0, 2, 4, 6, 8, 10\}$', size='s')
a, b, c, rr = (21.0, 44.0), (63.5, 44.0), (44.0, 20.0), 3.6
arrow(ax, (21, 58), (21, a[1] + rr), 'sujet'); arrow(ax, (63.5, 58), (63.5, b[1] + rr), 'autre')
disc(ax, *a, rr, 'sujet', label='3'); disc(ax, *b, rr, 'autre', label='2')
text(ax, 21 + 6, 51, r'$h = 3$', 'sujet', 's', ha='left'); text(ax, 63.5 - 6, 51, r'$k = 2$', 'autre', 's', ha='right')
box(ax, 3, 4, 82, 28, 'resultat', fill=False, dash=True)
for p in (a, b):
    s, e = short(p, c, rr + 0.4); arrow(ax, s, (e[0], e[1] + 0.0), 'varie')
disc(ax, *c, rr, 'resultat', label='5')
text(ax, 66, 20, r'$hk = 3 + 2 = 5$', 'resultat', 's')
text(ax, 83, 7, r'$HK$ : toutes les sommes', 'resultat', 's', ha='right')
save(fig, '50-062')
