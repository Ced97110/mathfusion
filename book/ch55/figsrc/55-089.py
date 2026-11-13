import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [44, 58, 72]
w, h = 12, 10
for i, x in enumerate(xs):
    text(ax, x + w / 2, 50, rf'$x_{i + 1}$', 'fixe', 'm')
rows = [(r'$x_1^2\,x_3$', (2, 0, 1), 30), (r'$x_1\,x_2\,x_3$', (1, 1, 1), 8)]
for lab, ks, y in rows:
    text(ax, 16, y + h / 2, lab, 'sujet', 'l')
    arrow(ax, (31, y + h / 2), (41, y + h / 2), 'varie')
    for x, k in zip(xs, ks):
        if k == 0:
            box(ax, x, y, w, h, 'fixe', fill=False, label='0', dash=True)
        else:
            box(ax, x, y, w, h, 'sujet', label=str(k))
text(ax, 58, 43.5, 'un exposant par variable', 'fixe', 's')
save(fig, '55-089')
