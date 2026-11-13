import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 41, 60, '2,3', 'fixe', 'l', weight='bold', ha='right')
text(ax, 41.5, 60, '5', 'sujet', 'l', weight='bold', ha='left')
x0, cw = 8, 7.2
for i in range(10):
    box(ax, x0 + i * cw, 24, cw, 9, 'sujet' if i < 5 else 'fixe', fill=True, lw=0.6, r=0.1)
text(ax, x0, 18.5, '2,3', 'fixe', 's'); text(ax, x0 + 10 * cw, 18.5, '2,4', 'fixe', 's')
brace(ax, x0, x0 + 5 * cw, 36, 'sujet', '5 centièmes', down=False)
arrow(ax, (41.5, 56), (41.5, 47), 'sujet')
text(ax, 44, 9, '1 dixième = 10 parts', 'fixe', 's')
text(ax, x0 + 2.5 * cw, 28.5, '5/100', 'encre', 's')
save(fig, '08-027')
