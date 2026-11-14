import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
# header: the two unknowns
box(ax, 28, 38, 28, 11, 'sujet', label=r'$x$ : 1er nombre', size='s')
box(ax, 58, 38, 28, 11, 'autre', label=r'$y$ : 2e nombre', size='s')
rows = [('Cafés,\ncroissants', 'prix du café', 'prix du croissant', 20),
        ('Jus,\nthé', 'prix du jus', 'prix du thé', 3)]
for name, a, b, y in rows:
    box(ax, 2, y, 24, 13, 'fixe', label=name, size='s')
    box(ax, 28, y, 28, 13, 'sujet', label=a, size='s')
    box(ax, 58, y, 28, 13, 'autre', label=b, size='s')
for xc, role in ((42, 'sujet'), (72, 'autre')):
    arrow(ax, (xc, 37.5), (xc, 33.5), role, lw=0.9)
text(ax, 2 + 12, 43.5, 'problème', 'fixe', 's')
save(fig, '24-016')
