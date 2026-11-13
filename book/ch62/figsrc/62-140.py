import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = lambda x: (x ** 3 - 3 * x + 2) % 5
fp = lambda x: (3 * x ** 2 - 3) % 5
zf = {x for x in range(5) if f(x) == 0}
zp = {x for x in range(5) if fp(x) == 0}
assert zf == {1, 3} and zp == {1, 4}
text(ax, 44, 60, 'dans ℤ/5ℤ : pas de courbe', 'encre', 'm')
X = lambda x: 22 + 14 * x
box(ax, X(1) - 6.5, 22, 13, 32, 'resultat', fill=False, dash=True, lw=1.0)
for x in range(5):
    for y, z, role, g in ((46, zf, 'sujet', f), (30, zp, 'varie', fp)):
        if x in zf and x in zp:
            disc(ax, X(x), y, 3.2, 'resultat')
        elif x in z:
            disc(ax, X(x), y, 3.2, role)
        else:
            disc(ax, X(x), y, 3.2, 'fixe', fill=False)
    text(ax, X(x), 22.5 - 3.4, str(x), 'fixe', 's')
text(ax, 7, 46, r'$f$', 'sujet', 'l')
text(ax, 7, 30, r"$f\,'$", 'varie', 'l')
text(ax, X(1), 14, 'racine commune', 'resultat', 's')
text(ax, 44, 6, r"$(f,f\,')=x-1$ aussi modulo 5", 'encre', 's')
save(fig, '62-140')
