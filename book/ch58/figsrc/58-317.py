import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, 'ℤ/2ℤ = {0, 1}, toutes les familles', 'encre', 's')
rows = [
    ('famille vide', (True, False), 'n’engendre pas 1'),
    ('famille (1)', (True, True), 'liée : 2 × 1 = 0'),
    ('2 éléments ou plus', (True, True), 'liée : 2 × x = 0'),
]
y = 52
for name, gen, verdict in rows:
    text(ax, 2, y + 4.5, name, 'fixe', 's', ha='left')
    for i, g in enumerate(gen):
        disc(ax, 8 + i * 12, y - 2, 3.4, 'sujet' if g else 'fixe', label=str(i), size='s')
    text(ax, 33, y - 2, 'engendre' if all(gen) else 'engendre 0', 'sujet', 's', ha='left')
    box(ax, 56, y - 6.5, 30, 9, 'limite', label=verdict, size='s')
    y -= 17
text(ax, 44, 8, 'jamais génératrice ET indépendante', 'limite', 's', weight='bold')
save(fig, '58-317')
