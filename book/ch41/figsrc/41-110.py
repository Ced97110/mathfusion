import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u, v = (1, 2, 3), (4, 5, 6)
c = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
assert c == (-3, 6, -3)
neg = lambda n: str(n).replace('-', '−')
fig, ax = canvas(56)
w, g = 25, 5
x0 = (88 - 3 * w - 2 * g) / 2
box(ax, x0, 44, w, 9, 'sujet', label=r'$u=\langle 1, 2, 3\rangle$', size='s')
text(ax, x0 + w + g / 2, 48.5, '×', 'encre', 'm')
box(ax, x0 + w + g, 44, w, 9, 'autre', label=r'$v=\langle 4, 5, 6\rangle$', size='s')
text(ax, x0 + 2 * w + 1.5 * g, 48.5, '=', 'encre', 'm')
box(ax, x0 + 2 * w + 2 * g, 44, w, 9, 'resultat', label=r'$\langle -3, 6, -3\rangle$', size='s')
rows = [r'$2\times6-3\times5=-3$', r'$3\times4-1\times6=6$', r'$1\times5-2\times4=-3$']
for i, r in enumerate(rows):
    y = 30 - i * 11
    text(ax, 8, y + 4, f'{i + 1}', 'fixe', 'm')
    box(ax, 14, y, 66, 8, 'fixe', label=r, size='m')
text(ax, 44, 4, 'trois différences de deux produits croisés', 'encre', 's')
save(fig, '41-110')
