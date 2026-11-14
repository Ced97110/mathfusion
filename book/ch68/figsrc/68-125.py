import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(54)
text(ax, 44, 49, r'$x_1 = x_3 + x_5 + x_7$', 'resultat', 'l', weight='bold')

def plus(x, y):
    line(ax, [(x - 0.9, y), (x + 0.9, y)], 'encre', lw=1.0); line(ax, [(x, y - 0.9), (x, y + 0.9)], 'encre', lw=1.0)

for y, cap, b3, b5, b7, r in ((31, 'message 1001', 1, 0, 1, 0), (12, 'message 0110', 0, 1, 0, 1)):
    text(ax, 4, y + 8.5, cap, 'fixe', 's', ha='left')
    for x, name, v in ((4, 3, b3), (22, 5, b5), (40, 7, b7)):
        box(ax, x, y - 4, 15, 8, 'sujet', label=rf'$x_{name} = {v}$')
    plus(20.5, y); plus(38.5, y)
    arrow(ax, (56.5, y), (63.5, y), 'varie')
    box(ax, 64, y - 4, 20, 8, 'resultat', label=rf'$x_1 = {r}$')
crop(fig, ax, 4.9, 54.0)
save(fig, '68-125')
