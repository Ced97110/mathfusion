import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, 'les degrés des deux facteurs s’ajoutent', 'encre', 's')
rows = [(2, 1, 1), (3, 1, 2), (3, 2, 1)]
u = 9
y = 40
for tot, a, b in rows:
    text(ax, 4, y + 4, f'{tot} = {a} + {b}', 'encre', 'l', ha='left')
    x = 32
    for d in (a, b):
        role = 'resultat' if d == 1 else 'fixe'
        box(ax, x, y, d * u - 1.0, 8, role, label=str(d), size='m')
        x += d * u
    y -= 14
text(ax, 44, 7, 'toujours un facteur de degré 1', 'resultat', 'm', weight='bold')
save(fig, '54-206')
