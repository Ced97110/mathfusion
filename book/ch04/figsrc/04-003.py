import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)

# légende : la règle
box(ax, 4, 67, 5, 5, 'sujet')
text(ax, 11, 69.5, '1 case → 1 facteur 2', 'sujet', 'm', ha='left')
text(ax, 86, 69.5, 'case ajoutée : résultat × 2', 'varie', 's', ha='right')

# rangée A : 3 cases
for x in (4, 10, 16):
    box(ax, x, 55, 5, 5, 'sujet')
text(ax, 38, 57.5, '2 × 2 × 2 = 8', 'sujet', 'm', ha='left')

# rangée B : 4 cases, la 4e ajoutée
for x in (4, 10, 16, 22):
    box(ax, x, 46, 5, 5, 'varie' if x == 22 else 'sujet')
text(ax, 38, 48.5, '2 × 2 × 2 × 2 = 16', 'sujet', 'm', ha='left')

# rangée C : 5 cases, la 5e ajoutée
for x in (4, 10, 16, 22, 28):
    box(ax, x, 37, 5, 5, 'varie' if x == 28 else 'sujet')
text(ax, 38, 39.5, '2 × 2 × 2 × 2 × 2 = 32', 'sujet', 'm', ha='left')

# le résultat double d'une rangée à la suivante
for ya, yb in ((56, 49.5), (47, 40.5)):
    arrow(ax, (78, ya), (78, yb), 'varie')
    text(ax, 80, (ya + yb) / 2, '× 2', 'varie', 's', ha='left')

text(ax, 54, 30, 'un 2 oublié : 16 et non 32', 'limite', 's')

# rangée D : 20 cases étroites
text(ax, 4, 23, '20 cases :', 'sujet', 's', ha='left')
text(ax, 22, 23, '2 × 2 × … × 2', 'sujet', 's', ha='left')
for k in range(20):
    box(ax, 4 + 4*k, 14, 3.6, 5, 'sujet', lw=0.6)
brace(ax, 4, 83.6, 12, 'varie', label='20 facteurs 2 à compter', down=True, size='s')

save(fig, '04-003')
