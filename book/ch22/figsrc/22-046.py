import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(66)
text(ax, 44, 60, r'$\sqrt{x-3}$', 'sujet', 'l')
box(ax, 4, 8, 38, 44, 'resultat', fill=False)
text(ax, 23, 43, r'$x=5$', 'encre', 'm'); text(ax, 23, 31, r'$x-3=2$', 'encre', 'm'); text(ax, 23, 18, r'$\sqrt{2}$ existe', 'resultat', 'm')
box(ax, 46, 8, 38, 44, 'limite', fill=False)
text(ax, 65, 43, r'$x=1$', 'encre', 'm'); text(ax, 65, 31, r'$x-3=-2$', 'encre', 'm'); text(ax, 65, 18, 'pas de racine', 'limite', 'm')
save(fig, '22-046')
