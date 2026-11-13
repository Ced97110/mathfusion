import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(66)
for y, a, b in ((40, '25', '-5'), (14, '2', r'-\sqrt{2}')):
    box(ax, 4, y, 16, 11, 'fixe', label=a)
    arrow(ax, (22, y + 5.5), (34, y + 5.5), 'varie')
    box(ax, 36, y, 16, 11, 'autre', label='$' + b + '$')
    arrow(ax, (54, y + 5.5), (66, y + 5.5), 'varie')
    box(ax, 68, y, 16, 11, 'resultat', label=a)
text(ax, 28, 56, 'moins la racine', 'varie', 's')
text(ax, 60, 56, r'$\times$ elle-même', 'varie', 's')
save(fig, '22-041')
