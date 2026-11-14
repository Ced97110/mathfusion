import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$f(x)=x^3-2x^2+4$', 'sujet', 's')
x0, sx, base, sy = 14, 20.0, 22, 6.5   # x=0 -> 14 mm
X = lambda v: x0 + v * sx
f = lambda v: v ** 3 - 2 * v ** 2 + 4
line(ax, [(3, base), (85, base)], 'fixe')
line(ax, [(X(-0.6 + i * 0.05), base + f(-0.6 + i * 0.05) * sy) for i in range(0, 64)], 'sujet', lw=1.2)
ax.plot([X(1), X(1)], [base, base + 3 * sy], color=COL['resultat'], lw=1.6, zorder=4, solid_capstyle='round')
disc(ax, X(1), base + 3 * sy, 1.4, 'resultat')
text(ax, X(1), base - 4, r'$x=1$', 'fixe', 's')
text(ax, X(1) + 13, base + 3 * sy + 5, r'$f(1)=3$', 'resultat', 's')
box(ax, 3, 3, 40, 10, 'resultat', label=r'reste de $f$ par $x-1$ : 3')
box(ax, 46, 3, 39, 10, 'resultat', label=r'$3\neq0$ : 1 pas racine')
save(fig, '54-245')
