import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cols = [(16, r'$(\mathbb{Z}_8,+)$', 'groupe', 'fixe'), (44, r'$(\mathbb{Z}_8,\times)$', 'monoïde', 'fixe'), (72, r'$U(8)$', 'groupe', 'sujet')]
for cx, t, kind, role in cols:
    text(ax, cx, 76, t, 'sujet' if role == 'sujet' else 'fixe', 'm', weight='bold')
    text(ax, cx, 70, kind, role, 's')
ys = [60, 48, 36, 24]
for r, y in enumerate(ys):
    for dx in (-5, 5):
        disc(ax, 16 + dx, y, 3.6, 'fixe')
    disc(ax, 44 - 5, y, 3.6, 'fixe')
    disc(ax, 44 + 5, y, 3.6, 'limite')
    disc(ax, 72, y, 3.6, 'sujet', label=str([1, 3, 5, 7][r]), size='s')
text(ax, 16, 14, '8 éléments', 'fixe', 's')
text(ax, 44, 14, '8 éléments', 'fixe', 's')
text(ax, 72, 14, '4 éléments', 'sujet', 's')
text(ax, 44, 7, 'rouge : sans inverse', 'limite', 's')
save(fig, '44-171')
