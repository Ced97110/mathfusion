import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
a, b, q = 7 + 2j, 2 + 1j, 3 - 1j
r = a - b * q
ex = a / b
assert r == 1j and abs(ex - (3.2 - 0.6j)) < 1e-12 and (b * b.conjugate()).real == 5 and (r * r.conjugate()).real == 1
text(ax, 44, 53, r'$7+2i=(2+i)(3-i)+i$', 'encre', 'l')
text(ax, 44, 45.5, r'taille du reste $1$ < taille de $b$ $5$', 'resultat', 's')
x0, y0, k = 18, 29, 20    # position de la valeur (2, 0) ; k mm par unité
P = lambda re, im: (x0 + (re - 2) * k, y0 + im * k)
for re in (2, 3, 4):
    for im in (0, -1):
        disc(ax, *P(re, im), 1.0, 'fixe')
for re in (2, 3, 4):
    text(ax, P(re, 0)[0], y0 + 4.5, str(re), 'fixe', 's')
text(ax, 7, y0, r'$0i$', 'fixe', 's'); text(ax, 6.5, y0 - k, r'$-i$', 'fixe', 's')
ex_pt, q_pt = P(3.2, -0.6), P(3, -1)
line(ax, [q_pt, ex_pt], 'varie', lw=1.2)
disc(ax, *q_pt, 2.4, 'resultat')
disc(ax, *ex_pt, 1.8, 'varie')
text(ax, q_pt[0] - 4, q_pt[1] - 5.5, 'arrondi\n' + r'$q=3-i$', 'resultat', 's', ha='right')
text(ax, ex_pt[0] + 4, ex_pt[1] + 3.5, 'exact\n' + r'$3{,}2-0{,}6i$', 'varie', 's', ha='left')
text(ax, 64, 11, 'erreur d’arrondi :\n$0{,}2$ et $0{,}4$', 'varie', 's', ha='left')
save(fig, '56-176')
