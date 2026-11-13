import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, 'fractions essayées, au carré', 'encre', 's')
data = [(r'$(7/5)^2$', r'$1{,}96<2$'), (r'$(17/12)^2$', r'$2{,}0069>2$'), (r'$(99/70)^2$', r'$2{,}0002>2$')]
for i, (a, b) in enumerate(data):
    y = 54 - i * 14
    box(ax, 4, y, 34, 11, 'fixe', label=a, size='m')
    arrow(ax, (39, y + 5.5), (45, y + 5.5), 'varie')
    box(ax, 46, y, 38, 11, 'varie', label=b, size='m')
text(ax, 44, 17, 'proches de 2, jamais égaux à 2', 'varie', 's')
box(ax, 4, 3, 80, 9, 'autre', label='il faut une démonstration', size='m')
save(fig, '12-126')
