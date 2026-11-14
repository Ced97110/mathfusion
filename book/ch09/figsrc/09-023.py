import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [('8', 'gallons'), ('32', 'cents'), ('54', 'miles')]
text(ax, 25, 56, 'nombre', 'sujet', 's'); text(ax, 56, 56, 'unité', 'autre', 's')
for i, (n, un) in enumerate(rows):
    y = 38 - i * 14
    box(ax, 14, y, 22, 10, 'sujet', label=n, size='l')
    box(ax, 36, y, 32, 10, 'autre', label=un, size='l')
text(ax, 44, 4, 'un nombre + une unité', 'encre', 's')
save(fig, '09-023')
