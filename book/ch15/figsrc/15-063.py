import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for cx, c, e in ((22, '5', '3'), (66, '3', '5')):
    box(ax, cx - 18, 22, 36, 22, 'fixe')
    text(ax, cx - 7, 30, c, 'fixe', 'xl'); text(ax, cx + 1, 30, r'$x$', 'encre', 'xl')
    text(ax, cx + 4.5, 35, e, 'sujet', 'l', weight='bold')
    text(ax, cx + 6.5, 54, 'degré', 'sujet', 'm'); arrow(ax, (cx + 4.5, 51), (cx + 4.5, 39), 'sujet')
    text(ax, cx - 7, 10, 'coefficient', 'fixe', 'm'); arrow(ax, (cx - 7, 13), (cx - 7, 26), 'fixe')
save(fig, '15-063')
