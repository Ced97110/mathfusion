import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
etapes = [
    ('1. diviser', r'$40 = 13\times3 + 1$', 'sujet'),
    ('2. isoler 1', r'$1 = 40 - 13\times3$', 'sujet'),
    ('3. ramener', r'$-13 + 40 = 27$', 'varie'),
    ('4. vérifier', r'$3\times27 = 81 = 2\times40 + 1$', 'resultat'),
]
for i, (nom, formule, role) in enumerate(etapes):
    y = 68 - i * 21
    text(ax, 3, y + 6, nom, role, 'm', ha='left')
    box(ax, 28, y, 58, 12, role, label=formule)
    if i < 3:
        arrow(ax, (57, y - 0.5), (57, y - 8.5), 'varie')
save(fig, '53-089')
