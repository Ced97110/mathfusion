import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
U, OX, OY = 10, 10, 10
P = lambda x, y: (OX + U * x, OY + U * y)
for i in range(4):
    for j in range(3):
        disc(ax, *P(i, j), 0.6, 'fixe')
line(ax, [P(2, 0), P(2, 1)], 'fixe', dash=True)
line(ax, [P(1, 0), P(1, 1)], 'fixe', dash=True)
arrow(ax, P(0, 0), P(1, 0), 'fixe', lw=1.3)
arrow(ax, P(0, 0), P(0, 1), 'fixe', lw=1.3)
arrow(ax, P(0, 0), P(2, 1), 'varie', lw=1.3)
arrow(ax, P(0, 0), P(1, 1), 'autre', lw=1.3)
text(ax, 15, 6.5, '$e_1$', 'fixe', 'm')
text(ax, 7, 15, '$e_2$', 'fixe', 'm')
text(ax, 32.5, 22, '$f_1$', 'varie', 'm')
text(ax, 20, 24, '$f_2$', 'autre', 'm')
def cell(x, y, v, role):
    text(ax, x, y, v, role, 'm')
cx, cy, cw, rh = 66, 34, 7.0, 7.0
x0, y0 = cx - cw, cy - rh
for sx, d in ((x0 - 0.8, 1), (x0 + 2 * cw + 0.8, -1)):
    line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + 2 * rh + 0.4), (sx + 1.3 * d, y0 + 2 * rh + 0.4)], 'fixe', lw=0.9)
vals = [['2', '1'], ['1', '1']]
for i in range(2):
    for j in range(2):
        cell(x0 + (j + 0.5) * cw, y0 + 2 * rh - (i + 0.5) * rh, vals[i][j], 'varie' if j == 0 else 'autre')
text(ax, cx, 46, '$P$', 'encre', 'm')
text(ax, cx, 21, '$f_1=2e_1+1e_2$', 'varie', 's')
text(ax, cx, 14, '$f_2=1e_1+1e_2$', 'autre', 's')
save(fig, '58-225')
