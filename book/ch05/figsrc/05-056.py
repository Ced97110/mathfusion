import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def cross(x, y, role='encre'):
    line(ax, [(x - 1.3, y - 1.3), (x + 1.3, y + 1.3)], role, lw=0.9)
    line(ax, [(x - 1.3, y + 1.3), (x + 1.3, y - 1.3)], role, lw=0.9)
text(ax, 44, 60, r'$60 = 2 \times 30 = 2 \times 2 \times 15$', 'fixe', 'm')
ya, yb = 44, 20
xs = [26, 40, 54, 68]
text(ax, 4, ya, r'$60 =$', 'encre', 'm', ha='left')
for k, (x, v) in enumerate(zip(xs, [2, 2, 3, 5])):
    disc(ax, x, ya, 4.5, 'resultat', label=str(v))
    if k: cross((xs[k-1] + x) / 2, ya)
text(ax, 4, yb, r'$60 =$', 'encre', 'm', ha='left')
pos = [32, 52, 66]
box(ax, pos[0] - 7, yb - 5.5, 14, 11, 'varie', fill=True)
text(ax, pos[0], yb, r'$2^2$', 'varie', 'l')
disc(ax, pos[1], yb, 4.5, 'resultat', label='3'); disc(ax, pos[2], yb, 4.5, 'resultat', label='5')
cross(43, yb); cross(59, yb)
arrow(ax, (xs[0] + 1.5, ya - 5), (pos[0] - 3, yb + 5.7), 'varie')
arrow(ax, (xs[1] - 1.5, ya - 5), (pos[0] + 3, yb + 5.7), 'varie')
arrow(ax, (xs[2], ya - 5), (pos[1] + 1, yb + 5.2), 'fixe')
arrow(ax, (xs[3], ya - 5), (pos[2], yb + 5.2), 'fixe')
text(ax, 44, 8.5, r'$2^2$ : le 2 est écrit 2 fois', 'varie', 's')
text(ax, 44, 3.5, '3 et 5 : une seule fois (exposant 1)', 'fixe', 's')
save(fig, '05-056')
