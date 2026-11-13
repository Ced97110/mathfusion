import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
arrow(ax, (14, 10), (56, 10), 'fixe', lw=0.9)
arrow(ax, (14, 10), (14, 52), 'fixe', lw=0.9)
text(ax, 61, 10, r'$s_1$', 'fixe', 's')
text(ax, 14, 56, r'$s_2$', 'fixe', 's')
for k in range(3):
    text(ax, 20 + 14 * k, 5.5, str(k), 'fixe', 's')
    text(ax, 9.5, 16 + 14 * k, str(k), 'fixe', 's')
for i in range(3):
    for j in range(3):
        hi = (i, j) == (1, 2)
        ax.add_patch(Circle((20 + 14 * i, 16 + 14 * j), 1.9, ec=COL['varie' if hi else 'sujet'],
                            fc=COL['varie' if hi else 'sujet'], zorder=3))
text(ax, 34, 49, r'$(1, 2)$', 'varie', 's')
text(ax, 73, 38, r'$r = 2$ copies' + '\nde ' + r'$F$', 'sujet', 's')
text(ax, 73, 24, r'$F \times F$ :' + '\n' + r'$3 \times 3 = 9$ points', 'sujet', 's')
save(fig, '55-045')
