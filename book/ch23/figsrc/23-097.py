import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X0, Y0, sx, sy = 14, 14, 10.0, 3.0
f = numberline(ax, X0, X0 + 6 * sx, Y0, 0, 6)
g = lambda x: (x - 3) ** 2
pts = [(f(0.4 + i * 0.05), Y0 + sy * g(0.4 + i * 0.05)) for i in range(int((5.6 - 0.4) / 0.05) + 1)]
line(ax, pts, 'sujet', lw=1.3)
for x in range(1, 6):
    v = g(x); r = 'resultat' if v == 0 else 'sujet'
    ax.plot([f(x)], [Y0 + sy * v], 'o', color=COL[r], ms=3.5, zorder=4)
    text(ax, f(x), Y0 + sy * v + 4.5 if v else Y0 + 5, f'{v:g}', r, 'm')
text(ax, 44, 57, r'$y=x^2-6x+9$', 'sujet', 'l')
text(ax, 44, 48, r'$D=0$', 'resultat', 'l')
text(ax, 44, 42, 'un seul zéro', 'resultat', 's')
save(fig, '23-097')
