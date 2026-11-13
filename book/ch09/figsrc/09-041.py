import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, '« par » = « pour chaque »', 'varie', 'm', weight='bold')
rows = [('15 miles', 'gallon'), ('4 euros', 'kilo'), ('12 litres', 'minute')]
for k, (a, b) in enumerate(rows):
    y = 38 - k * 16
    box(ax, 4, y, 25, 10, 'sujet', label=a)
    box(ax, 31, y, 11, 10, 'varie', label='par')
    box(ax, 44, y, 8, 10, 'fixe', label='1', dash=True)
    box(ax, 54, y, 30, 10, 'autre', label=b)
text(ax, 48, 2.5, '1 : nombre caché', 'fixe', 's')
save(fig, '09-041')
