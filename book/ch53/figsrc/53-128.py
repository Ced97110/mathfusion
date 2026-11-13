import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(68)
rows = [
    (50, ('p = 5', 'autre'), ('q = 11', 'autre'), '×', ('n = 55', 'sujet', 'm')),
    (30, ('p − 1 = 4', 'autre'), ('q − 1 = 10', 'autre'), '×', ('φ = 40', 'autre', 'm')),
    (10, ('e = 3', 'sujet'), ('φ = 40', 'autre'), 'et', ('PGCD(3, 40) = 1', 'resultat', 's')),
]
for y, a, b, op, res in rows:
    box(ax, 2, y, 22, 11, a[1], label=a[0])
    text(ax, 27.5, y + 5.5, op, 'encre', 'm')
    box(ax, 31, y, 22, 11, b[1], label=b[0])
    arrow(ax, (55, y + 5.5), (62, y + 5.5), 'varie')
    box(ax, 63, y, 23, 11, res[1], label=res[0], size=res[2])
save(fig, '53-128')
