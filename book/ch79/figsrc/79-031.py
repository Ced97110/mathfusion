import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def edge(a, b, r, role, lw=0.9):
    dx, dy = b[0] - a[0], b[1] - a[1]; k = r / math.hypot(dx, dy)
    line(ax, [(a[0] + dx * k, a[1] + dy * k), (b[0] - dx * k, b[1] - dy * k)], role, lw)
n4, n12, n20, n60 = (44, 10), (28, 34), (60, 34), (44, 58)
for a, b in [(n4, n12), (n4, n20), (n12, n60), (n20, n60)]: edge(a, b, 4.2, 'fixe')
edge(n4, n12, 4.2, 'resultat', 2.4)
for p, n, r in [(n4, '4', 'sujet'), (n12, '12', 'resultat'), (n20, '20', 'fixe'), (n60, '60', 'limite')]: disc(ax, p[0], p[1], 4.2, r, label=n)
text(ax, 18, 21, '12 recouvre 4', 'resultat', 's')
text(ax, 51, 58, '60 ne recouvre pas 4 :', 'limite', 's', ha='left'); text(ax, 51, 54, '12 est entre 4 et 60', 'limite', 's', ha='left')
save(fig, '79-031')
