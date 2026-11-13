import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, w, g = 7.5, 16, 3
for i in range(3):
    box(ax, x0 + i * (w + g), 42, w, 8, 'sujet')
text(ax, x0 + (3 * w + 2 * g) / 2, 55, '3 tablettes', 'sujet')
text(ax, 44, 35.5, '1 chacune : il en faut 4', 'encre')
for i in range(4):
    cx = x0 + i * (w + g) + w / 2
    if i < 3:
        box(ax, cx - w / 2, 22, w, 8, 'sujet')
    else:
        box(ax, cx - w / 2, 22, w, 8, 'limite', fill=False, dash=True, label='manque', size='s')
    disc(ax, cx, 12, 3, 'autre')
    arrow(ax, (cx, 15.5), (cx, 21), 'fixe')
text(ax, 44, 4, '4 personnes', 'autre')
save(fig, '06-001')
