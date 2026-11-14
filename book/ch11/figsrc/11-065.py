import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
ws = [14, 14, 14, 18]; labs = ['2', 'h', '40', 'min']; g = 3
x = (88 - sum(ws) - 3 * g) / 2; y = 30
for w, l in zip(ws, labs):
    isn = l in ('2', '40')
    box(ax, x, y, w, 12, 'sujet' if isn else 'fixe', label=l, size='l')
    text(ax, x + w / 2, y - 3.5, 'nombre' if isn else 'unité', 'sujet' if isn else 'fixe', 's')
    x += w + g
arrow(ax, (44, 22), (44, 15), 'varie')
text(ax, 44, 9, 'même durée : 160 min', 'resultat', 'm')
save(fig, '11-065')
