import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
X0, Y0, sx, sy = 6, 14, 70 / 9, 5.0
f = numberline(ax, X0, X0 + 9 * sx, Y0, -4, 5, labels=False, arrow_right=False)
for c, r, a, b, lab in [(3, 'sujet', 1.4, 4.6, r'$x^2-6x+9$'), (-2, 'autre', -3.6, -0.4, r'$x^2+4x+4$')]:
    n = 40
    xs = [a + (b - a) * i / n for i in range(n + 1)]
    line(ax, [(f(x), Y0 + sy * (x - c) ** 2) for x in xs], r, lw=1.3)
    ax.plot([f(c)], [Y0], 'o', color=COL['resultat'], ms=4, zorder=4)
    text(ax, f(c), Y0 - 4, str(c).replace('-', '−'), r, 'm')
    text(ax, f(c), 49, lab, r, 'm')
    text(ax, f(c), 42, r'$=(x%+d)^2$' % (-c), r, 'm')
text(ax, f(0.5), 33, r'$D=0$', 'resultat', 'l')
text(ax, f(0.5), 5, 'touche l’axe', 'resultat', 's')
save(fig, '23-098')
