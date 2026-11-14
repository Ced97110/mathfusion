import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs = [18, 38, 58, 78]
for x, n in zip(xs, ['95', '97', '98', '99']):
    box(ax, x - 8, 66, 16, 9, 'sujet', label=n)
def fus(cx, w, y, label, k):
    box(ax, cx - w / 2, y, w, 9, 'resultat', label=label)
    text(ax, 2, y + 4.5, f'fusion {k}', 'varie', 's', ha='left')
fus(28, 20, 48, '9215', 1)
fus(43, 24, 30, '903 070', 2)
fus(60, 28, 12, '89 403 930', 3)
arrow(ax, (xs[0], 66), (24, 57.2), 'varie'); arrow(ax, (xs[1], 66), (32, 57.2), 'varie')
arrow(ax, (28, 48), (38, 39.2), 'varie'); arrow(ax, (xs[2], 66), (48, 39.2), 'varie')
arrow(ax, (43, 30), (54, 21.2), 'varie'); arrow(ax, (xs[3], 66), (66, 21.2), 'varie')
save(fig, '52-256')
