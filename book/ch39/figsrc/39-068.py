import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# cis 30° × cis 45° : le terme avec i × i donne le signe moins
fig, ax = canvas(76)
cw, ch = 33, 14
cols = [20, 54]
rows = [44, 28]
text(ax, 8, 64, '×', 'fixe', 'm')
for cx, s in zip(cols, ['cos 45°', 'i sin 45°']):
    text(ax, cx + cw / 2, 64, s, 'fixe', 'm')
for ry, s in zip(rows, ['cos 30°', 'i sin 30°']):
    text(ax, 10, ry + ch / 2, s, 'fixe', 's')
cells = [(0, 0, 'cos 30° cos 45°', 'fixe'), (1, 0, 'i cos 30° sin 45°', 'fixe'),
         (0, 1, 'i sin 30° cos 45°', 'fixe'), (1, 1, 'i² sin 30° sin 45°\n= −sin 30° sin 45°', 'varie')]
for c, r, s, role in cells:
    box(ax, cols[c], rows[r], cw, ch, role, label=s, size='s', lw=1.6 if role == 'varie' else 0.8)
text(ax, 70.5, 24, 'i × i = −1', 'varie', 's', weight='bold')
arrow(ax, (70.5, 28), (70.5, 20.6), 'varie', lw=0.9)
box(ax, 2, 4, 84, 10, 'resultat', label='partie réelle = cos 30° cos 45° − sin 30° sin 45°', size='s')
save(fig, '39-068')
