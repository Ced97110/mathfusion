import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ax.add_patch(Circle((30, 44), 22, ec=COL['sujet'], fc='none', lw=1.0, zorder=2))
ax.add_patch(Circle((58, 44), 22, ec=COL['autre'], fc='none', lw=1.0, zorder=2))
text(ax, 22, 72, 'diviseurs de 5', 'sujet', 's'); text(ax, 66, 72, 'diviseurs de 8', 'autre', 's')
disc(ax, 20, 44, 3.2, 'sujet', label='5', size='s')
disc(ax, 44, 44, 3.6, 'resultat', label='1', size='s')
for k, v in enumerate([2, 4, 8]):
    disc(ax, 58 + k * 8.5, 44, 3.2, 'autre', label=str(v), size='s')
text(ax, 44, 12, 'PGCD = 1 : image à 1 élément', 'resultat', 's')
arrow(ax, (44, 20), (44, 16.5), 'resultat') if False else None
save(fig, '48-170')
