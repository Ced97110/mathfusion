import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$f(x) = (x-a_1)(x-a_2)(x-a_3)/4$', 'sujet', 's')
# courbe : racines 1, 2, 3
x0, sx, base, sy = 6, 17.0, 50, 14.0   # x=0 -> 6 mm ; 17 mm par unité
X = lambda v: x0 + v * sx
f = lambda v: (v - 1) * (v - 2) * (v - 3) / 4
line(ax, [(3, base), (83, base)], 'fixe')
pts = [(X(0.25 + i * 0.05), base + f(0.25 + i * 0.05) * sy) for i in range(0, 62)]
line(ax, pts, 'sujet', lw=1.2)
for k, a in enumerate((1, 2, 3), 1):
    disc(ax, X(a), base, 1.5, 'resultat')
    text(ax, X(a), base - 5, rf'$a_{k}$', 'resultat', 's')
# facteurs
for k, a in enumerate((1, 2, 3), 1):
    xa = X(a)
    box(ax, xa - 7.5, 18, 15, 9, 'sujet', label=rf'$x-a_{k}$')
    arrow(ax, (xa, base - 8), (xa, 28.5), 'fixe')
text(ax, 44, 11, r'degrés $1+1+1=3$', 'resultat', 's')
text(ax, 44, 4.5, 'un 4e point demanderait degré 4', 'limite', 's')
save(fig, '54-236')
