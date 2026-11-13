import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
k = 14 / 5
def cv(x0, fn, role, n=60):
    line(ax, [(x0 + 34 * i / n, 26 + 5 * k * fn(math.pi * i / n)) for i in range(n + 1)], role, lw=1.6)
line(ax, [(6, 26), (40, 26)], 'fixe'); line(ax, [(52, 26), (86, 26)], 'fixe')
cv(6, math.sin, 'autre'); cv(52, math.sin, 'autre'); cv(52, math.cos, 'sujet')
disc(ax, 6, 26, 1.5, 'resultat')
disc(ax, 52, 26, 1.5, 'autre'); disc(ax, 52, 40, 1.5, 'sujet')
line(ax, [(52, 26 + 3 * k), (86, 26 + 3 * k)], 'limite', dash=True)
disc(ax, 52, 26 + 3 * k, 1.5, 'limite')
text(ax, 2, 55, 'départ à 0', 'resultat', 'm', ha='left')
text(ax, 50, 55, 'départ à 3', 'limite', 'm', ha='left')
text(ax, 23, 8, r'$\sin 0 = 0$  : correct', 'resultat', 's')
text(ax, 69, 8, 'aucun ne donne 3', 'limite', 's')
text(ax, 23, 46, 'sin', 'autre', 's'); text(ax, 58, 46, 'cos', 'sujet', 's'); text(ax, 70, 46, 'sin', 'autre', 's')
text(ax, 47, 40, '5', 'sujet', 's', ha='right'); text(ax, 47, 26 + 3 * k, '3', 'limite', 's', ha='right'); text(ax, 47, 26, '0', 'autre', 's', ha='right')
save(fig, '30-168')
