import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
rows = [
    ('Facile des deux côtés', True, True),
    ('Difficile des deux côtés', False, False),
    ('Ce qu’il faut à Léa', True, False),
]
for i, (titre, aller, retour) in enumerate(rows):
    top = 84 - i * 28
    role = 'sujet' if i == 2 else 'fixe'
    text(ax, 3, top, titre, role, 'm', ha='left', weight='bold')
    ya, yr = top - 8, top - 16
    arrow(ax, (6, ya), (46, ya), 'resultat' if aller else 'fixe', lw=1.8 if aller else 0.6)
    arrow(ax, (46, yr), (6, yr), 'resultat' if retour else 'fixe', lw=1.8 if retour else 0.6)
    text(ax, 26, ya + 3, r'$f$ : ' + ('facile' if aller else 'difficile'), 'encre', 's')
    text(ax, 26, yr - 3, r'$f^{-1}$ : ' + ('facile' if retour else 'difficile'), 'encre', 's')
box(ax, 56, 84 - 56 - 22, 30, 12, 'varie', label='info de Léa')
arrow(ax, (55.5, 84 - 56 - 16), (47, 84 - 56 - 16), 'varie')
save(fig, '53-079')
