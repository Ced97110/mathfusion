import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
Y = lambda v: 8 + 14 * v
line(ax, [(16, 6), (16, 52)], 'fixe')
for v, lab in [(0, '0'), (0.5, '0,5'), (1, '1'), (2, '2')]:
    line(ax, [(15, Y(v)), (17, Y(v))], 'fixe')
    text(ax, 13, Y(v), lab, 'fixe', 'm', ha='right')
for v, role, lab in [(0.5, 'sujet', 'y = 0,5'), (2, 'autre', 'y = 2')]:
    line(ax, [(16, Y(v)), (82, Y(v))], role, lw=1.3)
    for x in (24, 34, 44, 54):
        disc(ax, x, Y(v), 0.9, role)
    text(ax, 70, Y(v) + 3.5, lab, role, 'm')
text(ax, 44, 58, 'y = k : points à hauteur k', 'encre', 'm')
save(fig, '32-016')
