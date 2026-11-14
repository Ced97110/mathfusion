import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

u = 5.8
fig, ax = canvas(76)
A = (8, 14)
line(ax, [A, (A[0] + 12 * u, 14)], 'sujet', lw=1.6)
for k in (1, 2, 3):
    x = A[0] + 4 * k * u
    line(ax, [(x, 14), (x, 14 + 3 * k * u)], 'varie', lw=1.6)
    ax.plot([x], [14 + 3 * k * u], 'o', color=COL['encre'], ms=3, zorder=4)
    ax.plot([x], [14], 'o', color=COL['sujet'], ms=2, zorder=4)
    text(ax, x, 9.5, str(4 * k), 'sujet', 's')
    text(ax, x + 2.8, 14 + 1.5 * k * u, str(3 * k), 'varie', 's')
    text(ax, x - 3.5, 14 + 3 * k * u + 3, r'$B_%d$' % k, 'encre', 'm')
line(ax, [A, (A[0] + 12 * u, 14 + 9 * u)], 'encre', lw=1.1)
arc(ax, A, 10, 0, 36.87, 'fixe', 1.0)
text(ax, 4.5, 10, r'$A$', 'encre', 'm')
text(ax, 30, 60, '3/4 = 6/8 = 9/12', 'resultat', 'm')
text(ax, 30, 54, 'rapport 0,75', 'resultat', 's')
save(fig, '25-015')
