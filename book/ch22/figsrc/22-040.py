import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(56)
text(ax, 12, 38, r'$x=25$', 'fixe', 's')
box(ax, 4, 18, 16, 14, 'fixe', label='25')
arrow(ax, (22, 25), (34, 25), 'varie'); text(ax, 28, 30, 'racine', 'varie', 's')
box(ax, 36, 18, 14, 14, 'sujet', label='5')
arrow(ax, (52, 25), (64, 25), 'varie'); text(ax, 58, 30, r'$\times\,5$', 'varie', 's')
box(ax, 66, 18, 18, 14, 'resultat', label='25')
brace(ax, 4, 84, 16, 'resultat', 'retour au départ', True, 'm')
save(fig, '22-040')
