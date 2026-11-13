import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(60)
text(ax, 4, 54, 'la calculatrice affiche', 'fixe', 'm', ha='left')
box(ax, 4, 38, 22, 11, 'fixe', label=r'$\sqrt{16}$')
arrow(ax, (28, 43.5), (44, 43.5), 'fixe')
box(ax, 46, 38, 14, 11, 'resultat', label='4')
text(ax, 4, 28, 'vous ajoutez le signe moins', 'varie', 'm', ha='left')
box(ax, 4, 12, 8, 11, 'varie', label=r'$-$')
box(ax, 14, 12, 22, 11, 'fixe', label=r'$\sqrt{16}$')
arrow(ax, (38, 17.5), (54, 17.5), 'fixe')
box(ax, 56, 12, 18, 11, 'resultat', label=r'$-4$')
save(fig, '22-037')
