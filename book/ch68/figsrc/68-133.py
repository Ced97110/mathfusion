import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(104)
CX = 52
G = ['1101', '1011', '1000', '0111', '0100', '0010', '0001']
ys = [84 - 6.4 * j for j in range(7)]
xs, p = bitrow(fig, ax, CX, 96, '1001', 'encre', k=7)
roles = ['varie', 'fixe', 'fixe', 'varie']
cells(ax, xs, p, 96, 7, roles)
text(ax, 18, 96, r'$m$ =', 'sujet', 'xl')
yc = (ys[0] + ys[-1]) / 2
for x, r in zip(xs, roles):
    cell(ax, x, yc, p - 1, 7 * 6.4, r)
for y, s in zip(ys, G):
    bitrow(fig, ax, CX, y, s, 'encre', k=7)
xl, xr = xs[0] - p / 2 - 1.2, xs[-1] + p / 2 + 1.2
for x, d in ((xl, 1.6), (xr, -1.6)):
    line(ax, [(x + d, ys[0] + 3.4), (x, ys[0] + 3.4), (x, ys[-1] - 3.4), (x + d, ys[-1] - 3.4)], 'sujet', lw=1.1)
text(ax, 18, yc, r'$G$', 'sujet', 'xl')
xw, pw = bitrow(fig, ax, CX, 36, '1110000', 'varie', k=7)
bitrow(fig, ax, CX, 28.5, '1101001', 'varie', k=7)
line(ax, [(xw[0] - 5, 24), (xw[-1] + 5, 24)], 'encre', lw=1.0)
bitrow(fig, ax, CX, 18, '0011001', 'resultat', k=7)
for y, s in ((36, 'colonne 1'), (28.5, 'colonne 4')):
    text(ax, 2, y, s, 'varie', 's', ha='left')
line(ax, [(17.2, 28.5), (19.6, 28.5)], 'encre', lw=1.0); line(ax, [(18.4, 27.3), (18.4, 29.7)], 'encre', lw=1.0)
text(ax, 8, 18, r'$c$', 'resultat', 'xl')
crop(fig, ax, 13.9, 104.0)
save(fig, '68-133')
