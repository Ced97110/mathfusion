import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'lecture 1 : un élément de S', 'sujet', 'm', weight='bold')
for i in range(6):
    role = 'varie' if i == 3 else 'fixe'
    box(ax, 9.5 + i * 12, 48, 9, 9, role, label=r'$s$' if i == 3 else None)
text(ax, 44, 43, 'une place quelconque de S', 'sujet', 's')
line(ax, [(4, 37), (84, 37)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 32, 'lecture 2 : la fonction identité', 'autre', 'm', weight='bold')
box(ax, 4, 11, 28, 11, 'autre', label=r'entrée $s$')
box(ax, 56, 11, 28, 11, 'autre', label=r'sortie $s$')
arrow(ax, (33, 16.5), (55, 16.5), 'varie')
text(ax, 44, 21.5, r'$s \mapsto s$', 'varie', 'm')
text(ax, 44, 11.5, 'recopie', 'varie', 's')
save(fig, '55-032')
