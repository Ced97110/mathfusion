import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 22, 78, 'ce que vous saviez', 'sujet', 's'); text(ax, 68, 78, 'son nom', 'resultat', 's')
rows = [(r'$3 + 5 = 5 + 3$', 'commutatif'), (r'$(2+3)+4 = 2+(3+4)$', 'associatif'), (r'$n + 0 = n$', 'neutre 0')]
for i, (a, b) in enumerate(rows):
    y = 66 - i * 14
    box(ax, 2, y - 5, 46, 10, 'sujet', label=a, size='s')
    box(ax, 58, y - 5, 28, 10, 'resultat', label=b, size='s')
    arrow(ax, (48.5, y), (57.5, y), 'varie')
text(ax, 44, 30, '+ opposé, + inverse : groupe', 'autre', 's')
box(ax, 2, 10, 40, 10, 'autre', label=r'$(\mathbb{R}, +)$ : opposé', size='s')
box(ax, 46, 10, 40, 10, 'autre', label=r'$(\mathbb{R}^*, \times)$ : inverse', size='s')
save(fig, '44-278')
