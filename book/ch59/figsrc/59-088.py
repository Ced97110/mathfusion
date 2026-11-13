import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 25.5, 56, 'mineurs d’ordre 1', 'sujet', 's')
for i, v in enumerate(['4', '6', '6', '4']):
    box(ax, 4 + i * 11, 40, 10, 11, 'sujet', label=v)
arrow(ax, (48, 45.5), (56, 45.5), 'varie')
text(ax, 52, 41, 'PGCD', 'varie', 's')
box(ax, 57, 40, 28, 11, 'resultat', label=r'$\Delta_1=2$')
text(ax, 12, 30, 'mineur d’ordre 2', 'autre', 's', ha='left')
box(ax, 4, 14, 20, 11, 'autre', label=r'$-20$')
arrow(ax, (25, 19.5), (56, 19.5), 'varie')
text(ax, 40, 15, 'valeur absolue', 'varie', 's')
box(ax, 57, 14, 28, 11, 'resultat', label=r'$\Delta_2=20$')
save(fig, '59-088')
