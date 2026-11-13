import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 24; ox, oy = 7, 14
Q = lambda x, y: (ox + u * x, oy + u * y)
poly(ax, [Q(0, 0), Q(1, 0), Q(1, 1), Q(0, 1)], 'fixe', fill=False, lw=0.7)
poly(ax, [Q(0, 0), Q(1, 0), Q(2, 1), Q(1, 1)], 'resultat')
line(ax, [Q(2, 1), Q(2, 0)], 'fixe', lw=0.7, dash=True)
text(ax, ox + u * 1.0, oy + u * 0.5, 'aire 1', 'resultat', 'm')
brace(ax, ox, ox + u, oy, 'resultat', 'base 1')
text(ax, ox + 2 * u + 2, oy + u / 2, 'hauteur 1', 'fixe', 's', ha='left')
for p, t in [(Q(1, 1), '(1, 1)'), (Q(2, 1), '(2, 1)')]:
    ax.add_patch(Circle(p, 0.9, fc=COL['resultat'], ec=COL['resultat'], zorder=6))
text(ax, ox + u * 1 - 3, oy + u + 3, '(1, 1)', 'resultat', 's')
text(ax, ox + u * 2 + 1, oy + u + 3, '(2, 1)', 'resultat', 's')
text(ax, ox - 1, oy + u + 3, 'carré', 'fixe', 's', ha='left')
text(ax, 44, 51, r'$(x,\,y)\mapsto(x+y,\,y)$', 'resultat', 'l')
text(ax, 44, 4, r'$\det=1$ : l’aire est gardée', 'resultat', 's')
save(fig, '73-020')
