import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$HG = A + A = 0$', 'sujet', 'l', weight='bold')
A = ['01', '10', '11']; Z = ['00'] * 3
ys = [35, 28, 21]
for c, rows, role in ((14, A, 'sujet'), (45, A, 'sujet'), (76, Z, 'resultat')):
    xs, p = bitrow(fig, ax, c, ys[0], rows[0], 'encre', k=5)
    cell(ax, c, ys[1], 2 * p + 0.5, 21, role)
    for y, s in zip(ys[1:], rows[1:]):
        bitrow(fig, ax, c, y, s, 'encre', k=5)
    for x, d in ((c - p - 2.4, 1.4), (c + p + 2.4, -1.4)):
        line(ax, [(x + d, ys[0] + 4), (x, ys[0] + 4), (x, ys[-1] - 4), (x + d, ys[-1] - 4)], role, lw=1.0)
text(ax, 29.5, 28, '+', 'encre', 'xl')
text(ax, 60.5, 28, '=', 'encre', 'xl')
text(ax, 44, 8, '0 + 0 = 0 et 1 + 1 = 0', 'resultat', 'm')
crop(fig, ax, 4.2, 52.0)
save(fig, '68-140')
