import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(64)
cy, r = 30, 14
for cx, n, gens in [(22, 5, {1, 2, 3, 4}), (66, 6, {1, 5})]:
    disc(ax, cx, cy, r, 'fixe', fill=False)
    for k in range(n):
        p = P(cx, cy, r, 360 * k / n)
        disc(ax, p[0], p[1], 1.8 if k in gens else 1.2, 'resultat' if k in gens else 'fixe')
    text(ax, cx + r + 3.5, cy + 3, '1', 'fixe', 's')
    text(ax, cx, 54, r'$n=%d$ : %d générateurs' % (n, len(gens)), 'resultat', 's')
    text(ax, cx, 47, r'$\varphi(%d)=%d$' % (n, len(gens)), 'resultat', 'm')
text(ax, 44, 6, r'vert : engendre tout $U$', 'resultat', 's')
save(fig, '66-028')
