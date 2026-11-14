import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(66)
text(ax, 26, 59, 'nombre → carré', 'fixe', 'm'); text(ax, 66, 59, r'cherché : $-16$', 'autre', 'm')
for y, s in ((44, r'$4\;\to\;16$'), (32, r'$-4\;\to\;16$'), (20, r'$0\;\to\;0$')):
    box(ax, 6, y, 40, 9, 'fixe', label=s)
    text(ax, 66, y + 4.5, r'$\neq-16$', 'limite', 'm')
text(ax, 44, 9, 'aucun essai ne donne −16', 'limite', 'm')
save(fig, '22-043')
