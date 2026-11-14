import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$e=0{,}1$ : produit des racines $-0{,}39<0$', 'varie', 's')
f = numberline(ax, 10, 66, 62, -1, 4, 1, labels=False, arrow_right=True)
text(ax, f(0), 56.5, '0', 'fixe', 's')
r1, r2 = 2.933, -0.133
disc(ax, f(r1), 62, 1.4, 'resultat')
disc(ax, f(r2), 62, 1.4, 'fixe')
text(ax, f(r1), 68, r'$u\approx2{,}93$', 'resultat', 's')
text(ax, f(r2), 68, r'$u\approx-0{,}13$', 'fixe', 's')
text(ax, 77, 62, '$u$', 'fixe', 's')
g = numberline(ax, 10, 66, 20, -2, 2, 1, labels=False, arrow_right=True)
text(ax, g(0), 14.5, '0', 'fixe', 's')
x1 = r1 ** 0.5
for sx in (-1, 1):
    disc(ax, g(sx * x1), 20, 1.4, 'resultat')
    arrow(ax, (f(r1), 59.5), (g(sx * x1), 22.5), 'resultat', lw=0.9)
text(ax, g(-x1), 27, r'$x\approx-1{,}71$', 'resultat', 's')
text(ax, g(x1), 27, r'$x\approx1{,}71$', 'resultat', 's')
text(ax, 77, 20, '$x$', 'fixe', 's')
text(ax, f(r2) + 2, 49, r'$u<0$ : aucun $x$', 'fixe', 's')
save(fig, '70-113')
