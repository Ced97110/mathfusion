import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
Y0 = 40
def panel(X, sx, sy, a, b, fn, roots, title, nm, lab_dy=-4.5):
    arrow(ax, (X + sx * a - 1, Y0), (X + sx * b + 1, Y0), 'fixe', lw=0.9)
    n = 80
    line(ax, [(X + sx * x, Y0 + sy * fn(x)) for x in [a + (b - a) * i / n for i in range(n + 1)]], 'sujet', lw=1.3)
    for r in roots:
        ax.plot([X + sx * r], [Y0], 'o', color=COL['resultat'], ms=4, zorder=4)
        text(ax, X + sx * r, Y0 - 4.5, f'{r}'.replace('-', '−'), 'resultat', 's')
    text(ax, X + sx * (a + b) / 2, 66, title, 'sujet', 'm')
    text(ax, X + sx * (a + b) / 2, 5, nm, 'resultat', 'm')
panel(23, 10.0, 12.0, -1.4, 1.4, lambda x: x ** 3 - x, (-1, 0, 1), r'$x^3-x=0$', '3 solutions')
panel(52, 10.0, 2.1, -0.5, 2.5, lambda x: x ** 3 - 8, (2,), r'$x^3-8=0$', '1 solution')
save(fig, '23-108')
