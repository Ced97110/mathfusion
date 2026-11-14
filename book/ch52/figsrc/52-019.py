import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
CL = {0: 'sujet', 1: 'varie', 2: 'resultat', 3: 'limite'}
fig, ax = canvas(62)
rows = [(7, 1, 3, r'$7=1\times4+3$'), (-3, -1, 1, r'$-3=(-1)\times4+1$')]
for i, (n, k, r, s) in enumerate(rows):
    y = 48 - 18 * i
    disc(ax, 10, y, 4, CL[r], label=str(n).replace('-', '−'), size='m')
    text(ax, 40, y, s, 'encre', 'm')
    arrow(ax, (58, y), (63, y), 'fixe')
    box(ax, 64, y - 5, 22, 10, CL[r], label='reste %d' % r, size='m')
for r in range(4):
    x = 5 + r * 20.5
    box(ax, x, 6, 18, 8, CL[r], label='reste %d' % r, size='s')
text(ax, 44, 20, 'les quatre couleurs', 'fixe', 's')
save(fig, '52-019')
