import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
R = 3.6
xs = [12 + 16 * i for i in range(5)]
yt, yb = 48, 22

def edge(p, q, r):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    return (p[0] + dx / d * r, p[1] + dy / d * r)

# rangée du haut : sigma bouge 5 objets
for i, x in enumerate(xs):
    disc(ax, x, yt, R, 'sujet', label=str(i + 1))
for i in range(4):
    p, q = (xs[i], yt), (xs[i + 1], yt)
    arrow(ax, edge(p, q, R), edge(q, p, R), 'sujet')
arrow(ax, (xs[4], yt + R), (xs[0], yt + R), 'sujet', curve=0.25)
text(ax, 44, 64, r'$\sigma$ : 5 objets bougent', 'sujet', 'm')

# rangée du bas : le produit ne bouge que 1, 3, 5
for i, x in enumerate(xs):
    role = 'resultat' if i in (0, 2, 4) else 'fixe'
    disc(ax, x, yb, R, role, label=str(i + 1))
arrow(ax, (xs[0], yb + R), (xs[2], yb + R), 'resultat', curve=-0.45)
arrow(ax, (xs[2], yb + R), (xs[4], yb + R), 'resultat', curve=-0.45)
arrow(ax, (xs[4], yb - R), (xs[0], yb - R), 'resultat', curve=-0.3)
text(ax, xs[1], yb - 7, 'fixe', 'fixe', 's')
text(ax, xs[3], yb - 7, 'fixe', 'fixe', 's')
text(ax, 44, 39, r'$\sigma^{-1}\rho\sigma\rho^{-1}$ dans $N$', 'resultat', 'm')
text(ax, 44, 8, '3 objets bougent seulement', 'resultat', 's')
text(ax, 44, 2, r'$\rho$ ne touche que 1, 2, 3', 'fixe', 's')
save(fig, '64-128')
