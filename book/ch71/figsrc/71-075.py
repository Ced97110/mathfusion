import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, a, b, role, verdict):
    box(ax, 2, y, 26, 11, role, label=a)
    arrow(ax, (28, y + 5.5), (56, y + 5.5), 'varie')
    text(ax, 42, y + 10, r'$\times(\det P)^2\neq0$', 'varie', 's')
    box(ax, 56, y, 30, 11, role, label=b)
    text(ax, 44, y - 5, verdict, role, 's')
text(ax, 15, 63, 'base de départ', 'fixe', 's'); text(ax, 71, 63, 'autre base', 'fixe', 's')
row(38, r'$\det A=0$', r'$\det(P^TAP)=0$', 'limite', 'dégénérée dans toute base')
row(10, r'$\det A\neq0$', r'$\det(P^TAP)\neq0$', 'resultat', 'non dégénérée dans toute base')
save(fig, '71-075')
