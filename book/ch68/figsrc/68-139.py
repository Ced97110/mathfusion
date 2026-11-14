import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(80)
CX = 28
rows = ['10', '01', '01', '10', '11']
ys = [74 - 7 * j for j in range(5)]
xs, p = bitrow(fig, ax, CX, ys[0], rows[0], 'encre')
cell(ax, CX, (ys[0] + ys[1]) / 2, 2 * p + 0.5, 14, 'sujet')
cell(ax, CX, (ys[2] + ys[4]) / 2, 2 * p + 0.5, 21, 'varie')
for y, s in zip(ys[1:], rows[1:]):
    bitrow(fig, ax, CX, y, s, 'encre')
text(ax, 9, 60, r'$G$', 'sujet', 'xl')
text(ax, 42, (ys[0] + ys[1]) / 2, r'$I_k$ recopie le message', 'sujet', 'm', ha='left')
text(ax, 42, ys[3], r'$A$ calcule les contrôles', 'varie', 'm', ha='left')
for r, (m, w) in enumerate((('10', '10011'), ('01', '01101'), ('11', '11110'))):
    y = 36 - r * 11
    xm, pm = bitrow(fig, ax, 20, y, m, 'encre')
    cells(ax, xm, pm, y, 8, ['sujet'] * 2)
    arrow(ax, (32, y), (40, y), 'fixe')
    xw, pw = bitrow(fig, ax, 64, y, w, 'encre')
    cells(ax, xw, pw, y, 8, ['sujet'] * 2 + ['varie'] * 3)
crop(fig, ax, 6.8, 80.0)
save(fig, '68-139')
