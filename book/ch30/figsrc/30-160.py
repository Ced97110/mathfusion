import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ry = 36; k = 18 / 5
line(ax, [(2, ry), (86, ry)], 'fixe', dash=True)
text(ax, 3, ry + 2.2, 'repos', 'fixe', 's', ha='left')
for x, d, lab in [(28, 5, 'd = 5'), (54, 0, 'd = 0'), (78, -5, 'd = −5')]:
    y = ry + d * k
    if d != 0:
        s = 1 if d > 0 else -1
        arrow(ax, (x, ry), (x, y - s * 3.5), 'varie')
    disc(ax, x, y, 3.5, 'sujet')
    text(ax, x, y + (6.5 if d >= 0 else -6.5), lab, 'sujet', 'm')
save(fig, '30-160')
