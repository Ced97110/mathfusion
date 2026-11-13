import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy = 12, 8
X = lambda v: ox + v * 12
Y = lambda v: oy + v * 4.8
arrow(ax, (ox - 3, oy), (X(3.7), oy), 'fixe', lw=0.8); arrow(ax, (ox, oy - 3), (ox, Y(11.8)), 'fixe', lw=0.8)
line(ax, [(X(0), Y(1)), (X(3), Y(7))], 'sujet', lw=1.3); line(ax, [(X(0), Y(5)), (X(3), Y(11))], 'autre', lw=1.3)
text(ax, X(3) + 2, Y(7), r'$y = 2x + 1$', 'sujet', 's', ha='left'); text(ax, X(3) + 2, Y(11), r'$y = 2x + 5$', 'autre', 's', ha='left')
for x in (0.5, 1.5, 2.5):
    arrow(ax, (X(x), Y(2 * x + 1)), (X(x), Y(2 * x + 5)), 'varie', both=True)
    text(ax, X(x) + 2.5, Y(2 * x + 3), '4', 'varie', 's')
text(ax, 68, 24, 'écart toujours 4', 'varie', 'm')
save(fig, '43-036')
