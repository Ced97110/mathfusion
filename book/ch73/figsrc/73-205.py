import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))

fig, ax = canvas(88)
def row(y, a, b):
    f = numberline(ax, 10, 68, y, 0, 5, 1, every=5, arrow_right=False)
    arrow(ax, (f(0), y + 3), (f(a), y + 3), 'varie', curve=-0.45)
    arrow(ax, (f(a), y + 3), (f(5), y + 3), 'autre', curve=-0.35)
    text(ax, f(a / 2), y + 13, f'+ {a} x', 'varie', 's')
    text(ax, f((a + 5) / 2), y + 13, f'+ {b} x', 'autre', 's')
    dot(ax, (f(5), y), 'resultat', 1.8)
    text(ax, f(5) + 8, y, '5x', 'resultat', 's')
row(62, 2, 3)
row(22, 3, 2)
text(ax, 44, 44, 'même point d’arrivée', 'resultat', 's')
text(ax, 44, 80, 'multiples de x', 'fixe', 's')
save(fig, '73-205')
