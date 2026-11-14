import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
rows = [(30, '10', '60', '100'), (14, '25', '150', '190')]
for cy, a, b, c in rows:
    box(ax, 4, cy - 5, 16, 10, 'sujet', label=a, weight='bold')
    box(ax, 36, cy - 5, 16, 10, 'fixe', label=b)
    box(ax, 68, cy - 5, 16, 10, 'resultat', label=c, weight='bold')
    arrow(ax, (21, cy), (35, cy), 'varie'); arrow(ax, (53, cy), (67, cy), 'varie')
text(ax, 28, 42, '× 6', 'varie', 'l'); text(ax, 60, 42, '+ 40', 'varie', 'l')
text(ax, 44, 3.5, r'les deux gestes : $6n+40$', 'sujet', 'm')
save(fig, '15-002')
