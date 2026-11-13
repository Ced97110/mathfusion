import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(50)
r, y0 = 13, 18
a0, a1 = math.pi / 2 - 1, math.pi / 2 + 1
for cx in (16, 44, 72):
    pass
c1, c2, c3 = 16, 44, 72
a = arc(c1, y0, r, a0, a1); poly(ax, [(c1, y0)] + a, 'fixe')
b = arc(c2, y0, r, a0, a1); poly(ax, [(c2, y0), b[-1], b[0]], 'varie')
c = arc(c3, y0, r, a0, a1); poly(ax, c, 'resultat')
text(ax, c1, y0 - 3, r'$O$'); text(ax, a[-1][0] - 2.5, a[-1][1] + 1.5, r'$P$'); text(ax, a[0][0] + 2.5, a[0][1] + 1.5, r'$Q$')
text(ax, 30, 22, r'$-$', 'encre', 'xl'); text(ax, 58, 22, r'$=$', 'encre', 'xl')
text(ax, c1, 8, 'secteur : 9 cm²', 'fixe', 's')
text(ax, c2, 8, 'triangle OPQ', 'varie', 's')
text(ax, c3, 8, 'segment', 'resultat', 's')
text(ax, 44, 43, 'segment = secteur − triangle', 'encre', 'm')
save(fig, '29-097')
