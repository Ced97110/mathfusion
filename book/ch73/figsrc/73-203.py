import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))

fig, ax = canvas(72)
def panel(cx, vertical):
    o = (cx, 28)
    arrow(ax, (o[0] - 18, o[1]), (o[0] + 18, o[1]), 'fixe', lw=0.8)
    if vertical: arrow(ax, (o[0], o[1] - 14), (o[0], o[1] + 22), 'fixe', lw=0.8)
    return o
o1 = panel(23, False)
dot(ax, o1, 'limite', 2.0)
text(ax, 23, 62, 'somme de 3 carrés', 'sujet', 's')
text(ax, 23, 36, '(0, 0, 0)', 'limite', 's')
text(ax, 37, 23, 'espace', 'fixe', 's')
text(ax, 23, 8, 'aucun vecteur isotrope', 'limite', 's')
o2 = panel(65, True)
line(ax, [(o2[0] - 14, o2[1] - 14), (o2[0] + 14, o2[1] + 14)], 'resultat', lw=1.3)
dot(ax, (o2[0] + 10, o2[1] + 10), 'resultat', 2.0)
text(ax, 65, 62, 'moins le carré du temps', 'sujet', 's')
text(ax, 72, 51, 'temps', 'fixe', 's')
text(ax, 79, 23, 'espace', 'fixe', 's')
text(ax, 80, 36, '(1, 0, 0, 1)', 'resultat', 's', ha='right') if False else text(ax, 54, 46, '(1, 0, 0, 1)', 'resultat', 's')
text(ax, 65, 8, 'vecteur isotrope : Q = 0', 'resultat', 's')
save(fig, '73-203')
