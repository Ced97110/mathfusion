import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
els = [(k, 0) for k in range(4)] + [(k, 1) for k in range(4)]
def prod(a, b): return ((a[0] + (-1) ** a[1] * b[0]) % 4, (a[1] + b[1]) % 2)
x0, y0, c = 10, 14, 4.0
for i, a in enumerate(els):
    for j, b in enumerate(els):
        role = 'sujet' if prod(a, b)[1] == 0 else 'varie'
        poly(ax, [(x0 + j * c, y0 + 8 * c - (i + 1) * c), (x0 + (j + 1) * c, y0 + 8 * c - (i + 1) * c),
                  (x0 + (j + 1) * c, y0 + 8 * c - i * c), (x0 + j * c, y0 + 8 * c - i * c)], role, lw=0.3)
line(ax, [(x0 + 4 * c, y0), (x0 + 4 * c, y0 + 8 * c)], 'encre', lw=1.8); line(ax, [(x0, y0 + 4 * c), (x0 + 8 * c, y0 + 4 * c)], 'encre', lw=1.8)
line(ax, [(x0, y0), (x0 + 8 * c, y0), (x0 + 8 * c, y0 + 8 * c), (x0, y0 + 8 * c), (x0, y0)], 'encre', lw=1.8)
names = [['RR', 'RS'], ['SR', 'SS']]
for i in range(2):
    for j in range(2):
        text(ax, x0 + (2 + 4 * j) * c, y0 + (6 - 4 * i) * c, names[i][j], 'sujet' if i == j else 'varie', 'xl', weight='bold')
text(ax, 26, 59, r'table de $D_4$ : 64 cases', 'encre', 'm')
sx, sy, s = 56, 20, 12
for i in range(2):
    for j in range(2):
        box(ax, sx + j * s, sy + (1 - i) * s, s, s, 'sujet' if i == j else 'varie', lw=0.8, r=0.3, label=names[i][j], size='l', weight='bold')
text(ax, 68, 59, r'$D_4/\langle r\rangle$ : 4 cases', 'encre', 'm')
arrow(ax, (45, 30), (51.5, 30), 'varie')
box(ax, 8, 2.5, 3, 3, 'sujet', lw=0.5, r=0.2); text(ax, 13, 4, 'résultat : rotation', 'sujet', 's', ha='left')
box(ax, 46, 2.5, 3, 3, 'varie', lw=0.5, r=0.2); text(ax, 51, 4, 'résultat : retournement', 'varie', 's', ha='left')
save(fig, '47-157')
