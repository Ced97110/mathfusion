import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 20, 60, 'au sol', 'fixe', 's'); text(ax, 66, 60, 'sur le dessin', 'fixe', 's')
for xb in (8, 32):
    line(ax, [(xb, 22), (xb, 52)], 'sujet', lw=1.3)
ys_l = [24, 30, 36, 42, 48]
for y in ys_l:
    line(ax, [(8, y), (32, y)], 'varie', lw=1.1)
text(ax, 8, 18, r'$D_1$', 'sujet', 's'); text(ax, 32, 18, r'$D_2$', 'sujet', 's')
P = (66, 54)
for xb in (50, 82):
    line(ax, [(xb, 22), P], 'sujet', lw=1.3)
text(ax, 50, 18, r'$D_1$', 'sujet', 's'); text(ax, 82, 18, r'$D_2$', 'sujet', 's')
for yl, y in zip(ys_l, (25, 32, 39, 45, 50)):
    t = (54 - y) / (54 - 22); xl = 66 - 16 * t
    line(ax, [(33.5, yl), (xl - 1, y)], 'fixe', lw=0.5, dash=True)
    line(ax, [(xl, y), (66 + 16 * t, y)], 'varie', lw=1.1)
box(ax, 4, 3, 38, 8, 'sujet', label='rails : 2 droites', size='s')
box(ax, 46, 3, 38, 8, 'varie', label='traverses : mêmes barres', size='s')
save(fig, '80-279')
