import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
X0, Y0, u = 44, 40, 5.0
arrow(ax, (X0 - 20, Y0), (X0 + 24, Y0), 'fixe', lw=0.9)
line(ax, [(X0, Y0 - 22), (X0, Y0 + 28)], 'fixe')
n = 60
xs = [-3.0 + 6.0 * i / n for i in range(n + 1)]
line(ax, [(X0 + u * x, Y0 + u * (x * x - 4)) for x in xs], 'sujet', lw=1.3)
line(ax, [(X0 - 2 * u, Y0), (X0 + 2 * u, Y0)], 'resultat', lw=2.4)
for x, nm in ((-2, 'A'), (2, 'B')):
    ax.plot([X0 + u * x], [Y0], 'o', color=COL['encre'], ms=3.5, zorder=4)
    text(ax, X0 + u * x + (-3 if x < 0 else 3), Y0 + 3.5, nm, 'encre', 'm')
    text(ax, X0 + u * x + (-4 if x < 0 else 4), Y0 - 3.8, f'{x}'.replace('-', '−'), 'fixe', 's')
text(ax, X0, Y0 - 9, r'$y<0$', 'resultat', 's')
text(ax, X0, Y0 - 29, r'$-2<x<2$', 'resultat', 'l')
text(ax, 12, 62, r'$y=x^2-4$', 'sujet', 'm')
save(fig, '23-101')
