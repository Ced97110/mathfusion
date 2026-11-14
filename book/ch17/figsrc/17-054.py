import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 22, 86, 'équation', 'sujet', 'm', weight='bold')
text(ax, 66, 86, 'inéquation', 'autre', 'm', weight='bold')
rows = [(r'$3x+1=10$', r'$3x+1<10$'), (r'$3x=9$', r'$3x<9$'), (r'$x=3$', r'$x<3$')]
steps = ['on retire 1', 'on divise par 3']
for i, (a, b) in enumerate(rows):
    y = 66 - i * 25
    box(ax, 4, y, 36, 11, 'sujet', label=a)
    box(ax, 48, y, 36, 11, 'autre', label=b)
    if i < 2:
        arrow(ax, (22, y - 0.5), (22, y - 13.5), 'varie')
        arrow(ax, (66, y - 0.5), (66, y - 13.5), 'varie')
        text(ax, 44, y - 7, steps[i], 'varie', 's')
text(ax, 44, 4, 'mêmes gestes : seul le signe change', 'fixe', 's')
save(fig, '17-054')
