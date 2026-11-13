import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, r'$\frac{1}{x} < 2$, on multiplie par $x$', 'sujet', 'm')
def row(y, role, xl, mul, res, rrole, note):
    box(ax, 2, y, 22, 12, role, label=xl)
    arrow(ax, (26, y + 6), (54, y + 6), 'varie')
    text(ax, 40, y + 11, mul, 'varie', 's')
    box(ax, 56, y, 30, 12, rrole, label=res)
    text(ax, 71, y - 4, note, rrole, 's')
row(58, 'sujet', r'$x=4$', r'$\times 4$', r'$1 < 8$', 'fixe', 'le symbole reste')
row(30, 'autre', r'$x=-4$', r'$\times (-4)$', r'$1 > -8$', 'varie', 'le symbole se retourne')
box(ax, 14, 4, 60, 9, 'limite', label=r'$x=0$ : interdit')
save(fig, '17-126')
