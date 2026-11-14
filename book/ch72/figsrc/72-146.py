import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
o = (44, 38); u = 6
P = lambda x, y, z: iso(x, y, z, o, u)
def pl(pts, role):
    ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=FILL[role], alpha=0.75, lw=0.8, zorder=2))
pl([P(-3,-3,0), P(3,-3,0), P(3,3,0), P(-3,3,0)], 'sujet')
pl([P(-3,0,-3), P(3,0,-3), P(3,0,3), P(-3,0,3)], 'autre')
line(ax, [P(-3.4,0,0), P(3.4,0,0)], 'resultat', lw=2.2)
disc(ax, o[0], o[1], 1.0, 'encre')
text(ax, 44, 8, 'plan 1 : horizontal', 'sujet', 's')
text(ax, 44, 66, 'plan 2 : vertical', 'autre', 's')
text(ax, 44, 30, 'origine 0', 'encre', 's')
x1, y1 = P(3.4, 0, 0)
text(ax, x1 - 1, y1 + 5, 'axe : droite commune', 'resultat', 's', ha='right')
save(fig, '72-146')
