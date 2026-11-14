import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 60, 'choisi (libre)', 'varie', 'm')
text(ax, 66, 60, 'imposé', 'fixe', 'm')
for i, (a, b) in enumerate([(r'$x\mapsto 2$', ''), (r'$y\mapsto 3$', '')]):
    box(ax, 6, 42 - i * 14, 32, 10, 'varie', label=a)
rows = [('mot vide', r'$1$'), (r'$xyx$', r'$12$'), (r'$xy$', r'$6$')]
for i, (w, v) in enumerate(rows):
    y = 46 - i * 14
    box(ax, 48, y - 4, 20, 10, 'fixe', label=w, size='s')
    arrow(ax, (68.5, y + 1), (73, y + 1), 'fixe')
    text(ax, 80, y + 1, v, 'fixe', 'm')
text(ax, 22, 8, '2 choix', 'varie', 'm')
text(ax, 66, 8, 'tout le reste', 'fixe', 'm')
save(fig, '49-035')
