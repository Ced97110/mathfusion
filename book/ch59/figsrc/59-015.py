import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
s, ox, oy = 6.0, 8, 6
P = lambda x, y: (ox + x * s, oy + y * s)
inK = lambda x, y: any(4 * a + 6 * b == x and 6 * a + 4 * b == y for a in range(-12, 13) for b in range(-12, 13))
poly(ax, [P(0, 0), P(4, 6), P(10, 10), P(6, 4)], 'sujet')
n = 0
for i in range(13):
    for j in range(13):
        if inK(i, j):
            n += 1; ax.plot([P(i, j)[0]], [P(i, j)[1]], 'o', color=COL['sujet'], ms=3.4, zorder=4)
        else: ax.plot([P(i, j)[0]], [P(i, j)[1]], '.', color=COL['fixe'], ms=2.2, zorder=3)
assert n == 10, n
arrow(ax, P(0, 0), P(4, 6), 'sujet', lw=1.3)
arrow(ax, P(0, 0), P(6, 4), 'sujet', lw=1.3)
arrow(ax, P(0, 0), P(2, 3), 'varie', lw=1.6)
arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.6)
text(ax, P(4, 6)[0] - 6, P(4, 6)[1] + 2, r'$f_1$', 'sujet', 'm')
text(ax, P(6, 4)[0] + 6, P(6, 4)[1] - 2, r'$f_2$', 'sujet', 'm')
text(ax, P(2, 3)[0] - 7, P(2, 3)[1] + 2, r"$e'_1$", 'varie', 'm')
text(ax, P(1, 1)[0] + 7, P(1, 1)[1] - 3, r"$e'_2$", 'varie', 'm')
text(ax, P(6.5, 6.5)[0], P(6.5, 6.5)[1], 'aire 20', 'sujet', 'm', weight='bold')
text(ax, 84, 96, r'points bleus : $K$, qui se répètent', 'sujet', 's', ha='right')
text(ax, 84, 91, r"$e'_1,\ e'_2$ : tout le quadrillage", 'varie', 's', ha='right')
text(ax, 84, 86, r'$f_1,\ f_2$ : le parallélogramme', 'sujet', 's', ha='right')
save(fig, '59-015')
