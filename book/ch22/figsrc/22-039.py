import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(60)
text(ax, 4, 53, 'racine principale', 'sujet', 'm', ha='left')
y = 38
box(ax, 4, y, 18, 10, 'sujet', label='4'); text(ax, 27, y + 5, r'$\times$', 'encre', 'l')
box(ax, 32, y, 18, 10, 'sujet', label='4'); text(ax, 55, y + 5, '=', 'encre', 'l')
box(ax, 60, y, 20, 10, 'resultat', label='16')
text(ax, 4, 30, 'racine secondaire', 'autre', 'm', ha='left')
y = 16
box(ax, 4, y, 18, 10, 'autre', label=r'$-4$'); text(ax, 27, y + 5, r'$\times$', 'encre', 'l')
box(ax, 32, y, 18, 10, 'autre', label=r'$-4$'); text(ax, 55, y + 5, '=', 'encre', 'l')
box(ax, 60, y, 20, 10, 'resultat', label='16')
save(fig, '22-039')
