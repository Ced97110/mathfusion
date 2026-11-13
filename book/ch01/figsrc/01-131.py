import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
f = lambda k: 36 + 7*k
def d(x, y, role):
    disc(ax, x, y, 2.2, role); ax.patches[-1].set_zorder(3.5)
for y in (66, 44):
    line(ax, [(f(0), y), (f(6), y)], 'fixe')
    for k in range(7): line(ax, [(f(k), y-1.2), (f(k), y+1.2)], 'fixe', lw=0.8)
numberline(ax, 36, 78, 22, 0, 6, 1)
def arcs(y, ks, role):
    for k in ks: arrow(ax, (f(k), y+2.6), (f(k+1), y+2.6), role, curve=-0.6)
for k in range(7): d(f(k), 66, 'limite')
arcs(66, range(6), 'varie')
disc(ax, f(0), 66, 3.5, 'limite', fill=False)
text(ax, 2, 68.5, 'sans départ', 'limite', 'm', ha='left')
text(ax, 2, 63.5, 'n plus grand que n + 1', 'fixe', 's', ha='left')
for k in range(7): d(f(k), 44, 'resultat' if k <= 4 else 'limite')
arcs(44, range(4), 'varie'); arcs(44, [4], 'limite')
text(ax, 2, 46.5, 'sans passage', 'limite', 'm', ha='left')
text(ax, 2, 41.5, 'n plus petit que 5', 'fixe', 's', ha='left')
for k in range(7): d(f(k), 22, 'resultat')
arcs(22, range(6), 'varie')
text(ax, 2, 24.5, 'avec les deux', 'resultat', 'm', ha='left')
text(ax, 2, 19.5, 'la formule de la somme', 'fixe', 's', ha='left')
save(fig, '01-131')
