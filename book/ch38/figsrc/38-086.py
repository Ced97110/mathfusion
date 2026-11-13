import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(78)
# échelle : 1 km = 1 mm ; chaque longueur mesurée est 1 % plus grande
k = 1.0
rows = [(56, 'base', 12, '12,12'), (38, 'côté calculé', 50, '50,5'), (20, 'côté calculé', 8, '8,08')]
text(ax, 44, 74, 'une erreur de 1 % sur la base', 'encre', 'm')
for y, nom, v, vm in rows:
    text(ax, 4, y + 9, f'{nom} : {v} km', 'sujet', 's', ha='left')
    ax.add_patch(Rectangle((4, y), v * k, 3.2, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    ax.add_patch(Rectangle((4 + v * k, y), v * k * 0.01, 3.2, ec=COL['varie'], fc=COL['varie'], lw=0.8, zorder=3))
    text(ax, 4 + v * k + 3, y + 1.6, f'{vm} km', 'varie', 's', ha='left')
    text(ax, 80, y + 1.6, r'$\times1{,}01$', 'varie', 's')
text(ax, 44, 8, 'partout 1 % de plus : rien ne s’amplifie', 'varie', 's')
save(fig, '38-086')
