import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'monoïde libre : aucune égalité', 'sujet', 'm')
box(ax, 4, 52, 22, 10, 'sujet', label=r'$xy$')
box(ax, 30, 52, 22, 10, 'sujet', label=r'$yx$')
text(ax, 28, 46.5, 'deux mots distincts', 'sujet', 's')
arrow(ax, (55, 57), (62, 57), 'varie')
box(ax, 63, 49, 22, 16, 'varie', label=r'$xy=yx$')
arrow(ax, (74, 48), (74, 24), 'varie')
text(ax, 72, 44, 'on ajoute', 'varie', 's', ha='right')
text(ax, 72, 33, r'$x\mapsto 2,\ y\mapsto 3$', 'varie', 's', ha='right')
nums = ['1', '2', '3', '4', '6', '8', '9', '12']
for i, n in enumerate(nums):
    box(ax, 4 + i * 10.4, 14, 9, 9, 'resultat', label=n, size='s')
brace(ax, 4, 85, 12, 'resultat', label='puissances de 2 et de 3', down=True)
save(fig, '49-037')
