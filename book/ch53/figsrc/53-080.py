import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
rows = [
    ('clé publique : tout le monde', 10, 'autre'),
    ('clé privée : Léa seule', 1, 'sujet'),
    ('clé ancienne : 2 personnes', 2, 'fixe'),
]
for i, (titre, n, role) in enumerate(rows):
    y = 44 - i * 20
    text(ax, 4, y + 7, titre, role, 'm', ha='left', weight='bold' if role == 'sujet' else 'normal')
    for k in range(n):
        disc(ax, 7 + k * 8, y, 3, role)
save(fig, '53-080')
