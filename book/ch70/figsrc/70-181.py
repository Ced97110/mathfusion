import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, 'les carrés n² pour n = 0, 1, 2, …', 'encre', 's')
f = numberline(ax, 8, 70, 48, 0, 6, labels=False)
for v in (0, 1, 4):
    disc(ax, f(v), 48, 1.5, 'sujet'); text(ax, f(v), 42, f'{v}', 'sujet', 's')
ax.add_patch(Circle((f(2), 48), 1.5, fill=False, ec=COL['limite'], lw=1.2, zorder=4))
text(ax, f(2), 54.5, 'la cible 2', 'limite', 's')
text(ax, 78, 44, '…', 'sujet', 'm')
text(ax, 44, 35, 'entre 1 et 4 : pas de carré', 'limite', 's')
text(ax, 44, 26, 'même type d’équation', 'encre', 's')
box(ax, 2, 3, 41, 19, 'autre', label='entiers :\naucun calcul\ngénéral décide', size='s')
box(ax, 46, 3, 40, 19, 'resultat', label='réels :\nun calcul\ndécide', size='s')
save(fig, '70-181')
