import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

# x^3 - 3x + 1 : roots ~ 1.532, 0.347, -1.879 -> D = 9 ; x^3 - 2 : D^2 = -108
import math
r = [2 * math.cos(2 * math.pi * k / 9 + 0) for k in (0, 1, 2)]
rs = sorted([2 * math.cos(math.pi * 2 / 9), 2 * math.cos(math.pi * 4 / 9 + 0) , 2 * math.cos(math.pi * 8 / 9)], reverse=True)
Dv = (rs[0] - rs[1]) * (rs[0] - rs[2]) * (rs[1] - rs[2])
assert abs(Dv - 9) < 1e-9, Dv
fig, ax = canvas(76)
text(ax, 44, 71, r'$d=D^2=\prod(r_i-r_j)^2$', 'sujet', 'l', weight='bold')
text(ax, 16, 63, r'$D$', 'fixe', 'm', weight='bold')
text(ax, 44, 63, 'carré', 'fixe', 's')
text(ax, 72, 63, r'$d$', 'fixe', 'm', weight='bold')
rows = [(r'$x^3-3x+1$', 'D = 9', 'rationnel', 'd = 81', 40),
        (r'$x^3-2$', r'$D^2=-108$', 'D pas rationnel', 'd = −108', 14)]
for name, dtxt, note, dd, y in rows:
    text(ax, 3, y + 14, name, 'encre', 's', ha='left')
    box(ax, 4, y, 24, 10, 'varie', label=dtxt, size='s')
    arrow(ax, (28.5, y + 5), (58.5, y + 5), 'fixe', lw=0.9)
    box(ax, 59, y, 26, 10, 'resultat', label=dd, size='m', weight='bold')
    text(ax, 16, y - 3.5, note, 'varie', 's')
text(ax, 72, 6, r'$d\in F$ toujours', 'resultat', 's')
save(fig, '65-041')
