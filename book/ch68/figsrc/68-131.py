import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(74)
text(ax, 17, 69, 'message', 'fixe', 's')
text(ax, 62, 69, 'mot envoyé', 'fixe', 's')
data = [('1000', '1110000', 3), ('0100', '1001100', 5), ('0010', '0101010', 6), ('0001', '1101001', 7)]
for r, (m, w, q) in enumerate(data):
    y = 60 - r * 10.5
    xm, pm = bitrow(fig, ax, 17, y, m, 'encre', size='m', k=5)
    cell(ax, xm[r], y, pm - 0.8, 7, 'varie')
    arrow(ax, (31, y), (39, y), 'varie')
    xw, pw = bitrow(fig, ax, 62, y, w, 'encre', size='m', k=5)
    cell(ax, xw[q - 1], y, pw - 0.8, 7, 'varie')
text(ax, 44, 17, r'$1001 = 1000 + 0001$', 'sujet', 'l', weight='bold')
text(ax, 44, 9, 'donc la somme des deux mots', 'resultat', 'm')
crop(fig, ax, 5.2, 74.0)
save(fig, '68-131')
