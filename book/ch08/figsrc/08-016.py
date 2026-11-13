import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, x1 = 10, 78
y1, y2 = 50, 22
f1 = numberline(ax, x0, x1, y1, 2, 3, step=0.1, labels=False, arrow_right=False)
f2 = numberline(ax, x0, x1, y2, 2.3, 2.4, step=0.01, labels=False, arrow_right=False)
line(ax, [(f1(2.3), y1), (f1(2.4), y1)], 'varie', lw=2.2)
line(ax, [(x0, y2), (x1, y2)], 'varie', lw=2.2)
for v, ha_x in [(2, f1(2)), (3, f1(3))]:
    text(ax, ha_x, y1 - 5.2, f'{v}', 'fixe', 's')
text(ax, f1(2.3), y1 - 5.2, '2,3', 'varie', 's')
text(ax, f1(2.4), y1 - 5.2, '2,4', 'varie', 's')
text(ax, x0, y2 - 5.2, '2,3', 'varie', 's')
text(ax, x1, y2 - 5.2, '2,4', 'varie', 's')
text(ax, f2(2.35), y2 - 5.2, '2,35', 'sujet', 's')
line(ax, [(f1(2.3), y1 - 8.5), (x0, y2 + 2.5)], 'varie', dash=True)
line(ax, [(f1(2.4), y1 - 8.5), (x1, y2 + 2.5)], 'varie', dash=True)
for fx, y in [(f1, y1), (f2, y2)]:
    v = 2.35
    disc(ax, fx(v), y, 1.3, 'sujet')
    text(ax, fx(v), y + 5, r'$P$', 'sujet', 'm')
save(fig, '08-016')
