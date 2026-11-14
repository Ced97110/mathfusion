import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))

fig, ax = canvas(72)
def axes(cx):
    o = (cx, 34)
    arrow(ax, (o[0] - 17, o[1]), (o[0] + 17, o[1]), 'fixe', lw=0.8)
    arrow(ax, (o[0], o[1] - 17), (o[0], o[1] + 17), 'fixe', lw=0.8)
    return o
o1 = axes(23)
dot(ax, o1, 'limite', 2.0)
text(ax, 23, 62, 'x² + y²', 'sujet', 'm')
text(ax, 23, 44, '(0, 0)', 'limite', 's')
text(ax, 23, 10, 'aucun vecteur isotrope', 'limite', 's')
o2 = axes(65)
line(ax, [(o2[0] - 17, o2[1]), (o2[0] + 17, o2[1])], 'resultat', lw=1.8)
line(ax, [(o2[0], o2[1] - 17), (o2[0], o2[1] + 17)], 'resultat', lw=1.8)
dot(ax, (o2[0] + 11, o2[1]), 'resultat', 2.0)
text(ax, 65, 62, 'x y', 'sujet', 'm')
text(ax, o2[0] + 11, o2[1] - 6, '(1, 0)', 'resultat', 's')
text(ax, 65, 10, 'Q = 0 sur les axes', 'resultat', 's')
save(fig, '73-206')
