import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cols = {'c': 30, 'd': 44, 'u': 58}
for k, name in (('c', 'centaines'), ('d', 'dizaines'), ('u', 'unités')):
    text(ax, cols[k] + 6, 74, name, 'fixe', 's')
def cell(k, y, label, role='fixe'):
    if label is None:
        box(ax, cols[k], y, 12, 7, 'fixe', fill=False, dash=True)
    else:
        box(ax, cols[k], y, 12, 7, role, label=label)
def side(y, name, note, role):
    text(ax, 27, y + 3.5, name, role, 'm', ha='right')
    text(ax, 72, y + 3.5, note, role, 's', ha='left')
text(ax, 44, 67, 'sans zéro : plus long = plus grand', 'resultat', 's')
cell('c', 55, None); cell('d', 55, '1', 'resultat'); cell('u', 55, '2')
cell('c', 46, None); cell('d', 46, None); cell('u', 46, '7')
side(55, '12', 'plus long', 'resultat'); side(46, '7', 'plus court', 'resultat')
line(ax, [(6, 42), (82, 42)], 'fixe', lw=0.8, dash=True)
text(ax, 44, 37, 'avec zéros : 007 plus long, mais 7 < 12', 'limite', 's')
cell('c', 25, '0', 'limite'); cell('d', 25, '0', 'limite'); cell('u', 25, '7')
cell('c', 16, None); cell('d', 16, '1'); cell('u', 16, '2')
side(25, '007', 'plus long', 'limite'); side(16, '12', 'plus court', 'limite')
text(ax, 44, 9, 'le 0 ne compte aucun paquet', 'limite', 's')
save(fig, '01-103')
