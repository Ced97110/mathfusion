import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 83, r'$x^2+1$ sur $\mathbb{R}$ : aucune racine', 'sujet', 'm')
x0, y0, sx, sy = 44, 48, 12.0, 3.4
line(ax, [(x0 - 2.8 * sx, y0), (x0 + 2.8 * sx, y0)], 'fixe')
xs = [-2 + i * 0.05 for i in range(81)]
ax.plot([x0 + t * sx for t in xs], [y0 + (t * t + 1) * sy for t in xs], color=COL['sujet'], lw=1.2, zorder=3)
# le point le plus bas : valeur 1, jamais 0
disc(ax, x0, y0 + 1 * sy, 1.5, 'limite')
text(ax, x0, y0 - 5, r'valeur minimale 1, jamais $0$', 'limite', 's')
# factorisation complexe
box(ax, 4, 6, 80, 22, 'resultat')
text(ax, 44, 22, r'avec le nombre complexe $i$ ($i^2=-1$) :', 'resultat', 's')
text(ax, 44, 13, r'$x^2+1=(x-i)(x+i)$', 'resultat', 'm')
save(fig, '54-172')
