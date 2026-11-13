import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)

# grand chiffre : le facteur, écrit une fois
box(ax, 30, 46, 14, 14, 'sujet', label='3', size='l', weight='bold')
text(ax, 24, 53, 'le facteur', 'sujet', 's', ha='right')
arrow(ax, (25, 53), (29.5, 53), 'sujet')

# petit chiffre : combien de fois le facteur apparaît
box(ax, 45, 56, 7, 7, 'varie', label='2', size='m', weight='bold')
text(ax, 57, 59.5, 'nombre de fois', 'varie', 's', ha='left')
arrow(ax, (56.5, 59.5), (52.5, 59.5), 'varie')

# version longue de 3²
text(ax, 33, 38, '3² =', 'encre', 'm', ha='right')
text(ax, 35, 38, '3 × 3', 'encre', 'm', ha='left')
brace(ax, 35, 42.5, 35, 'varie', label='2 facteurs', down=True, size='s')

# version longue de 3⁵
text(ax, 33, 22, '3⁵ =', 'encre', 'm', ha='right')
text(ax, 35, 22, '3 × 3 × 3 × 3 × 3', 'encre', 'm', ha='left')
brace(ax, 35, 60, 19, 'varie', label='5 facteurs', down=True, size='s')

# erreur à éviter
box(ax, 22, 2.5, 44, 7, 'limite', fill=False, dash=True)
text(ax, 44, 6, "3² n'est pas 3 × 2 = 6", 'limite', 'm')

save(fig, '04-009')
