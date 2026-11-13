import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(56)
O = (10, 14); u = 5
Uend = (O[0] + 10 * u, 14); V = pol(O, 4 * u, 60); Hp = (V[0], 14)
arrow(ax, O, Uend, 'sujet', lw=1.8); arrow(ax, O, V, 'autre', lw=1.8)
line(ax, [V, Hp], 'fixe', dash=True)
line(ax, [O, Hp], 'varie', lw=3.2)
sq(ax, Hp, (-1, 0), (0, 1))
arc(ax, O, 8, 0, 60, 'fixe'); text(ax, 26, 19.5, '60°', 'fixe', 's')
text(ax, 38, 18.5, '10', 'sujet', 's'); text(ax, 11.5, 28, '4', 'autre', 's')
text(ax, 15, 9, '2', 'varie', 's')
text(ax, 58, 30, 'projection : 4 × 0,5 = 2', 'varie', 's')
text(ax, 58, 22, r'$10\times 2=20$', 'resultat', 'l', weight='bold')
text(ax, 44, 3, 'produit scalaire', 'resultat', 's')
save(fig, '26-126')
