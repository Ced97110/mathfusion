import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
heads = ['dixièmes', 'centièmes', 'millièmes']
cx0, cw = 24, 15
for c, h in enumerate(heads):
    text(ax, cx0 + cw * (c + .5), 56, h, 'fixe', 's')
rows = [('0,7', 0, '10'), ('0,07', 1, '100'), ('0,007', 2, '1000')]
for r, (n, pos, den) in enumerate(rows):
    y = 38 - r * 15
    text(ax, 11, y + 5.5, n, 'sujet', 'l')
    for c in range(3):
        on = c == pos
        box(ax, cx0 + cw * c, y, cw, 11, 'sujet' if on else 'fixe', fill=on, label='7' if on else None, size='l')
    text(ax, 79, y + 5.5, 'bas ' + den, 'resultat', 's')
save(fig, '08-033')
