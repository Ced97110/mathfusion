import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
x0, u, y0, v = 14, 11, 12, 11
for i in range(6):
    for j in range(4):
        if i != 3: disc(ax, x0 + i * u, y0 + j * v, 0.9, 'fixe')
line(ax, [(x0 + 3 * u, y0 - 2), (x0 + 3 * u, y0 + 3 * v + 5)], 'limite', lw=1.2)
for j in range(4): disc(ax, x0 + 3 * u, y0 + j * v, 1.7, 'limite')
f = numberline(ax, x0, x0 + 5 * u, 6, 0, 5, arrow_right=False)
for j in range(4): text(ax, 8, y0 + j * v, str(j), 'fixe', 's')
text(ax, x0 + 3 * u, 52, r'$x = 3$', 'limite', 'l')
text(ax, 44, 59.5, '3 a quatre images :\npas une application', 'limite', 'm', weight='bold')
save(fig, '42-306')
