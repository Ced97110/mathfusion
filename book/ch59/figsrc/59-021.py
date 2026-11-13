import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
s, ox, oy = 6.4, 8, 18
P = lambda x, y: (ox + x * s, oy + y * s)
for i in range(11):
    for j in range(11):
        ax.plot([P(i, j)[0]], [P(i, j)[1]], '.', color=COL['fixe'], ms=2.2, zorder=1)
arrow(ax, P(0, 0), P(4, 6), 'sujet', lw=1.5)
for k in (1, 2): disc(ax, *P(2 * k, 3 * k), 1.2, 'sujet')
arrow(ax, P(0, 0), P(10, 10), 'varie', lw=1.5)
for k in range(1, 11): disc(ax, *P(k, k), 0.9, 'varie')
line(ax, [P(4, 6), P(10, 10)], 'fixe', dash=True)
text(ax, P(4, 6)[0] - 9, P(4, 6)[1] + 3, r"$f_1=2e'_1$", 'sujet', 's')
text(ax, P(10, 10)[0] - 3, P(10, 10)[1] + 5, r"$f_1+f_2=10e'_2$", 'varie', 's', ha='right')
text(ax, P(7, 8)[0] - 3, P(7, 8)[1] + 5, r'$f_2$', 'fixe', 's')
text(ax, 8, 9, '2 pas de (2, 3)', 'sujet', 's', ha='left')
text(ax, 8, 3.5, '10 pas de (1, 1)', 'varie', 's', ha='left')
save(fig, '59-021')
