import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(76)
CX = 48
G = ['1101', '1011', '1000', '0111', '0100', '0010', '0001']
ys = [64 - 6.4 * j for j in range(7)]
xs, p = bitrow(fig, ax, CX, ys[0], G[0], 'encre', k=9)
yc = (ys[0] + ys[-1]) / 2
for x in xs:
    cell(ax, x, yc, p - 1, 7 * 6.4, 'sujet')
for y, s in zip(ys[1:], G[1:]):
    bitrow(fig, ax, CX, y, s, 'encre', k=9)
xl, xr = xs[0] - p / 2 - 1.2, xs[-1] + p / 2 + 1.2
for x, d in ((xl, 1.6), (xr, -1.6)):
    line(ax, [(x + d, ys[0] + 3.4), (x, ys[0] + 3.4), (x, ys[-1] - 3.4), (x + d, ys[-1] - 3.4)], 'sujet', lw=1.1)
text(ax, xl - 14, yc, r'$G$ =', 'sujet', 'xl', weight='bold')
text(ax, xl - 3.2, yc, '7 lignes', 'sujet', 's', rot=90)
brace(ax, xs[0] - p / 2, xs[-1] + p / 2, ys[0] + 5.2, 'sujet', label='4 colonnes = les 4 mots', down=False, depth=1.8)
crop(fig, ax, 18.8, 76.0)
save(fig, '68-132')
