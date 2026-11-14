import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'forme hermitienne sur…', 'varie', 'm')
rows = [(r'$\mathbb{C}$, conjugué', 'groupe unitaire', 'sujet', 'resultat'),
        ('quaternions, involution', 'troisième famille', 'autre', 'resultat')]
for i, (a, b, ra, rb) in enumerate(rows):
    y = 34 - i*22
    box(ax, 3, y, 38, 12, ra, label=a, size='s')
    box(ax, 56, y, 29, 12, rb, label=b, size='s')
    arrow(ax, (41.5, y+6), (55.5, y+6), 'varie')
text(ax, 44, 8, 'autres nombres, autre groupe', 'fixe', 's')
save(fig, '75-179')
