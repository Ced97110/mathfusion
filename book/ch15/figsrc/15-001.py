import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
for y, n in zip((36, 23, 10), (10, 25, 12)):
    box(ax, 3, y - 5, 36, 10, 'fixe')
    text(ax, 10, y, '6 ×', 'fixe'); text(ax, 21, y, str(n), 'varie', 'l', weight='bold'); text(ax, 31, y, '+ 40', 'fixe')
    arrow(ax, (40, y), (48, 23), 'varie')
box(ax, 49, 16.5, 36, 13, 'sujet')
text(ax, 56, 23, '6 ×', 'sujet'); text(ax, 66, 23, r'$n$', 'sujet', 'xl', weight='bold'); text(ax, 77, 23, '+ 40', 'sujet')
text(ax, 67, 9, 'n garde la place du nombre', 'varie', 's')
save(fig, '15-001')
