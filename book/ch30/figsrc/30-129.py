import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(r'$(0,\ 0)$', r'$(\pi/4,\ 1)$'), (r'$(\pi/2,\ 1)$', r'$(\pi/2,\ 3)$'),
        (r'$(\pi,\ 0)$', r'$(3\pi/4,\ 1)$'), (r'$(3\pi/2,\ -1)$', r'$(\pi,\ -1)$'),
        (r'$(2\pi,\ 0)$', r'$(5\pi/4,\ 1)$')]
text(ax, 18, 57, 'point de départ', 'fixe', 'm')
text(ax, 70, 57, 'point transformé', 'sujet', 'm')
for i, (a, b) in enumerate(rows):
    y = 47 - i * 9.5
    box(ax, 3, y - 3.5, 30, 7, 'fixe', label=a, size='m')
    box(ax, 55, y - 3.5, 30, 7, 'sujet', label=b, size='m')
    arrow(ax, (34, y), (54, y), 'varie')
save(fig, '30-129')
