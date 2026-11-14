import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert 2 * 3 == 6
fig, ax = canvas(72)
# 2 x 3 grid of unit cells = product
s = 8.0
x0, y0 = 8, 30
for i in range(3):
    for j in range(2):
        box(ax, x0 + i * s, y0 + j * s, s, s, 'sujet', r=0.2, lw=0.6)
text(ax, x0 + 12, y0 + 19, '3', 'sujet', 'm', weight='bold')
text(ax, x0 - 4, y0 + 8, '2', 'sujet', 'm', weight='bold')
text(ax, x0 + 12, y0 - 5, r'$r_1\times r_2$ : 6 cases', 'sujet', 's')
arrow(ax, (38, y0 + 8), (50, y0 + 8), 'varie', lw=1.0)
box(ax, 52, y0 + 2, 33, 12, 'sujet', label=r'$a_2=2\times3=6$', size='s', weight='bold')
text(ax, 44, 64, r'$x^2-5x+6$', 'encre', 'l')
text(ax, 68, 55, 'terme sans x : +6', 'varie', 's')
text(ax, 68, 48, 'même signe, +6', 'varie', 's') if False else None
text(ax, 44, 12, 'le 2 de a₂ est un rang,', 'fixe', 's')
text(ax, 44, 6, 'pas une puissance', 'fixe', 's')
save(fig, '65-047')
