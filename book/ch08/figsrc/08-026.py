import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 41, 60, '2,', 'fixe', 'l', weight='bold', ha='right')
text(ax, 41.5, 60, '3', 'sujet', 'l', weight='bold', ha='left')
text(ax, 46.5, 60, '5', 'fixe', 'l', weight='bold', ha='left')
f = numberline(ax, 6, 76, 28, 2, 3, 0.1, labels=False, arrow_right=False)
text(ax, f(2), 23.5, '2', 'fixe', 's'); text(ax, f(3), 23.5, '3', 'fixe', 's')
text(ax, f(2.3), 23.5, '2,3', 'sujet', 's', weight='bold')
for i in range(3):
    line(ax, [(f(2 + i / 10), 28), (f(2.1 + i / 10), 28)], 'sujet', lw=2.8)
    arrow(ax, (f(2 + i / 10) + 0.5, 31), (f(2.1 + i / 10) - 0.5, 31), 'varie', curve=-0.5)
brace(ax, f(2), f(2.3), 36, 'sujet', '3 dixièmes', down=False)
arrow(ax, (42.5, 56), (42.5, 47), 'sujet')
save(fig, '08-026')
