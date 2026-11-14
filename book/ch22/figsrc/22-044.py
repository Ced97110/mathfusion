import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(56)
y = 24
f = numberline(ax, 6, 76, y, -9, 9, 1, labels=False)
box(ax, 8, y + 4, 28, 14, 'limite', fill=False, dash=True, label='aucun carré négatif', size='s')
disc(ax, f(0), y, 2.2, 'resultat'); disc(ax, f(9), y, 2.2, 'resultat')
text(ax, f(0), y - 5, '0', 'resultat', 'm'); text(ax, f(9), y - 5, '9', 'resultat', 'm')
text(ax, f(0), y + 8, r'$0^2$', 'resultat', 's'); text(ax, f(9) - 4, y + 8, r'$3^2$ et $(-3)^2$', 'resultat', 's')
text(ax, 44, 8, 'valeur du carré', 'fixe', 's')
save(fig, '22-044')
