import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def nest(x0, labs, roles):
    box(ax, x0, 8, 36, 44, roles[0]); text(ax, x0 + 18, 48, labs[0], roles[0], 's')
    box(ax, x0 + 3, 11, 30, 32, roles[1]); text(ax, x0 + 18, 39, labs[1], roles[1], 's')
    box(ax, x0 + 6, 14, 24, 18, roles[2]); text(ax, x0 + 18, 23, labs[2], roles[2], 's')
nest(2, ["ℤ", "2ℤ", "4ℤ = noyau"], ['fixe', 'sujet', 'resultat'])
nest(50, [r"$\mathbb{Z}/4\mathbb{Z}$", r"$\{\bar0,\bar2\}$", r"$\{1'\}$"], ['fixe', 'sujet', 'resultat'])
arrow(ax, (50, 46), (38, 46), 'varie')
arrow(ax, (53, 36.5), (35, 36.5), 'varie')
arrow(ax, (56, 21), (32, 21), 'varie')
text(ax, 44, 51, r"$f^{-1}$", 'varie', 's')
text(ax, 44, 3, "le noyau est le plus petit", 'encre', 's')
save(fig, '48-068')
