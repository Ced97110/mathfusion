import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$p=x^2-4$ : où vaut-il $0$ ?', 'sujet', 'm')
x0, y0, sx, sy = 44, 40, 9.0, 3.2
line(ax, [(x0 - 3.6 * sx, y0), (x0 + 3.6 * sx, y0)], 'fixe')
xs = [-3 + i * 0.05 for i in range(121)]
ax.plot([x0 + t * sx for t in xs], [y0 + (t * t - 4) * sy for t in xs], color=COL['sujet'], lw=1.2, zorder=3)
for a in (-2, 2):
    disc(ax, x0 + a * sx, y0, 1.6, 'resultat')
    text(ax, x0 + a * sx, y0 + 5, f'$\\alpha={a}$'.replace('-', '-'), 'resultat', 's')
disc(ax, x0 + 3 * sx, y0 + 5 * sy, 1.6, 'fixe')
text(ax, x0 + 3 * sx - 1, y0 + 5 * sy + 5, r'$p(3)=5$', 'fixe', 's')
text(ax, 44, 21, r'$p(\alpha)=0$ : $\alpha$ est une racine', 'resultat', 'm')
text(ax, 44, 12, 'racines : 2 et $-2$ ; 3 n’en est pas une', 'encre', 's')
save(fig, '54-169')
