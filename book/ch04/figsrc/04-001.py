import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)

def grid(x0, y0, n):
    for i in range(n):
        for j in range(n):
            box(ax, x0 + 5*i, y0 + 5*j, 5, 5, 'sujet', lw=0.6, r=0)

# grilles
grid(8, 14, 3); grid(31, 14, 4); grid(59, 14, 5)

# traits verticaux (nombre de rangées) et leurs textes
line(ax, [(6.5, 14), (6.5, 29)], 'varie', lw=1.2)
line(ax, [(29.5, 14), (29.5, 34)], 'varie', lw=1.2)
line(ax, [(57.5, 14), (57.5, 39)], 'varie', lw=1.2)
text(ax, 4.5, 21.5, '3', 'varie', 's')
text(ax, 27.5, 24, '4', 'varie', 's')
text(ax, 55.5, 26.5, '5', 'varie', 's')

# accolades (carreaux par rangée)
brace(ax, 8, 23, 12.5, 'varie', label='3', down=True, size='s')
brace(ax, 31, 51, 12.5, 'varie', label='4', down=True, size='s')
brace(ax, 59, 84, 12.5, 'varie', label='5', down=True, size='s')

# produits au-dessus
text(ax, 15.5, 45, '3 × 3 = 9', 'resultat', 'm')
text(ax, 41, 45, '4 × 4 = 16', 'resultat', 'm')
text(ax, 71.5, 45, '5 × 5 = 25', 'resultat', 'm')

# règle
text(ax, 44, 3.5, 'les deux facteurs = le côté', 'encre', 's')

save(fig, '04-001')
