import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(62)
CX = 52
xs, p = bitrow(fig, ax, CX, 52, '0011001', 'encre')
cells(ax, xs, p, 52, 8, ['sujet'] * 7)
bitrow(fig, ax, CX, 43, '1110000', 'encre')
cells(ax, xs, p, 43, 8, ['limite'] * 3 + [''] * 4)
line(ax, [(xs[0] - 5, 38), (xs[-1] + 5, 38)], 'encre', lw=1.0)
bitrow(fig, ax, CX, 31, '1101001', 'encre')
cells(ax, xs, p, 31, 8, ['limite'] * 3 + ['autre'] * 4)
for y, s in ((52, 'envoyé c'), (43, 'erreur'), (31, 'reçu')):
    text(ax, 2, y, s, 'fixe', 's', ha='left')
line(ax, [(17.2, 43), (19.6, 43)], 'encre', lw=1.0); line(ax, [(18.4, 41.8), (18.4, 44.2)], 'encre', lw=1.0)
text(ax, 44, 19, 'aucun cercle impair', 'resultat', 'm', weight='bold')
text(ax, 44, 11, 'somme 0, mais 3 bits faux', 'limite', 'm', weight='bold')
crop(fig, ax, 6.9, 59.2)
save(fig, '68-148')
