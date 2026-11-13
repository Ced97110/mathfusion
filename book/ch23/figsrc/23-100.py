import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
X0, Y0, u = 40, 14, 7.0
arrow(ax, (X0 - 17, Y0), (X0 + 22, Y0), 'fixe', lw=0.9)
line(ax, [(X0, Y0 - 3), (X0, Y0 + 45)], 'fixe')
n = 60
xs = [-1.9 + 4.3 * i / n for i in range(n + 1)]
line(ax, [(X0 + u * x, Y0 + u * x * x) for x in xs], 'sujet', lw=1.3)
xs2 = [-2.0 + 4.4 * i / n for i in range(n + 1)]
line(ax, [(X0 + u * x, Y0 + u * (x + 2)) for x in xs2], 'autre', lw=1.3)
for x in (-1, 2):
    ax.plot([X0 + u * x], [Y0 + u * (x + 2)], 'o', color=COL['resultat'], ms=4, zorder=4)
    text(ax, X0 + u * x, Y0 - 4, f'$x={x}$', 'resultat', 's')
text(ax, 17, 58, r'$y=x^2$', 'sujet', 'm')
text(ax, 17, 22, r'$y=x+2$', 'autre', 'm')
text(ax, 70, 58, r'$D=9$', 'resultat', 'l')
text(ax, 70, 51, 'deux points', 'resultat', 's')
save(fig, '23-100')
