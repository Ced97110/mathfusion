import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ys = {0: 38, 1: 14}
arrow(ax, (6, ys[0]), (84, ys[0]), 'sujet', lw=1.0)
for i in range(4):
    x = 12 + 14 * i
    disc(ax, x, ys[0], 3.6, 'encre')
    text(ax, x, ys[0], str(i), 'varie', 's', weight='bold')
    disc(ax, x, ys[1], 3.6, 'limite', fill=False)
text(ax, 74, ys[0] + 5, '…', 'sujet', 'l')
text(ax, 4, 50, r'$n=0$ : ligne infinie', 'sujet', 'm', ha='left')
text(ax, 4, 4.5, r'$n=1$ : aucun numéro', 'limite', 'm', ha='left')
text(ax, 74, ys[1], '…', 'limite', 'l')
save(fig, '43-122')
