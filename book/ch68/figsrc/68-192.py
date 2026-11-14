import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(88)
text(ax, 44, 82, 'chaque facteur est pris ou laissé', 'encre', 's')
cx = [20, 42, 64]
for x, t in zip(cx, ['1 + x', '1 + x + x³', '1 + x² + x³']):
    text(ax, x, 74, t, 'sujet', 's')
ys = [66 - 7.2 * i for i in range(8)]
for i, y in enumerate(ys):
    bits = [(i >> 2) & 1, (i >> 1) & 1, i & 1]
    for x, b in zip(cx, bits):
        if b: cell(ax, x, y, 14, 5.6, 'sujet')
        else: cell(ax, x, y, 14, 5.6, 'fixe', fill=False, dash=True)
text(ax, 74, ys[0], '= 1', 'fixe', 's', ha='left')
text(ax, 74, ys[7], '= x⁷ + 1', 'fixe', 's', ha='left')
line(ax, [(73, ys[1] + 2.8), (75, ys[1] + 2.8), (75, ys[6] - 2.8), (73, ys[6] - 2.8)], 'resultat')
text(ax, 77, (ys[1] + ys[6]) / 2, '6 autres', 'resultat', 's', ha='left')
text(ax, 44, 8, '2 × 2 × 2 = 8 codes', 'resultat', 'l')
save(fig, '68-192')
