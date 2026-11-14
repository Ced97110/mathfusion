import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 13, 58, r'$m =$', 'sujet', 'xl')
text(ax, 38, 64, r'$y_2-y_1$', 'varie', 'l')
line(ax, [(24, 58), (52, 58)], 'fixe', lw=1.2)
text(ax, 38, 52, r'$x_2-x_1$', 'varie', 'l')
for y, t, r in [(64, 'on soustrait les y', 'varie'), (52, 'on soustrait les x', 'varie'), (58, 'on divise', 'resultat')]:
    text(ax, 59, y, t, r, 's', ha='left')
    arrow(ax, (58, y), (53 if y == 58 else 49, y), r, lw=0.8)
text(ax, 44, 42, 'mêmes actions, autres nombres', 'fixe', 's')
for x0, a, b in [(3, '(2, 5) et (6, 13)', '8 sur 4 = 2'), (46, '(0, 1) et (3, 7)', '6 sur 3 = 2')]:
    box(ax, x0, 6, 39, 28, 'sujet')
    text(ax, x0 + 19.5, 26, a, 'sujet', 'm')
    text(ax, x0 + 19.5, 14, b, 'resultat', 'l', weight='bold')
save(fig, '19-068')
