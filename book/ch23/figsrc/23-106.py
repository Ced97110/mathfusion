import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 3.0
X, Y = 6, 18
for i in range(8):
    line(ax, [(X + i * u, Y), (X + i * u, Y + 7 * u)], 'autre', lw=0.4)
    line(ax, [(X, Y + i * u), (X + 7 * u, Y + i * u)], 'autre', lw=0.4)
poly(ax, [(X, Y), (X + 7 * u, Y), (X + 7 * u, Y + 7 * u), (X, Y + 7 * u)], 'autre', fill=False, lw=1.0)
text(ax, X + 3.5 * u, Y - 4, 'côté 7', 'autre', 's')
text(ax, X + 3.5 * u, Y + 7 * u + 5, r'$x^2=49$', 'autre', 'm')
text(ax, X + 3.5 * u, 4, 'aire', 'autre', 's')
cubes(ax, [(i, j, k) for i in range(3) for j in range(3) for k in range(3)], (64, 14), 4.2, 'sujet')
text(ax, 64, 14 - 4.5, 'côté 3', 'sujet', 's')
text(ax, 64, Y + 7 * u + 5 + 6, r'$x^3=27$', 'sujet', 'm')
text(ax, 64, 4, 'volume', 'sujet', 's')
text(ax, 44, 59, r'$ax^3+bx^2+cx+d=0$', 'sujet', 'm')
save(fig, '23-106')
