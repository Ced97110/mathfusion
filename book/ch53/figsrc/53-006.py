import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
L = [(10, 56), (34, 56), (10, 32), (34, 32)]
R = [(x + 44, y) for x, y in L]
rr = 3.5
def seg(p, q):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    return [(p[0] + ux * rr, p[1] + uy * rr), (q[0] - ux * rr, q[1] - uy * rr)]
for a, b in itertools.combinations(L, 2):
    line(ax, seg(a, b), 'varie', lw=1.2)
for x, y in L: disc(ax, x, y, rr, 'fixe')
for x, y in R:
    disc(ax, x, y, rr, 'fixe')
    box(ax, x - 5.5, y - 10, 5, 3.5, 'varie', r=0.4)
    box(ax, x + 0.5, y - 10, 5, 3.5, 'autre', r=0.4)
text(ax, 22, 70, 'secrets partagés', 'encre', 'm')
text(ax, 66, 70, 'deux clés chacun', 'encre', 'm')
text(ax, 56, 19, 'clé publiée', 'varie', 's')
text(ax, 77, 19, 'clé gardée', 'autre', 's')
text(ax, 22, 12, '6 secrets, 6 rencontres', 'varie', 's')
text(ax, 66, 12, '4 paires, 0 rencontre', 'resultat', 's')
text(ax, 44, 4, '499 500 → 1 000 paires', 'encre', 'm')
save(fig, '53-006')
