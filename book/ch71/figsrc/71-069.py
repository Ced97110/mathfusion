import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def mat(x, y, w, h, v, role):
    box(ax, x, y, w, h, role)
    for k, s in enumerate(v):
        text(ax, x + w * (0.27 + 0.46 * (k % 2)), y + h * (0.72 - 0.44 * (k // 2)), s, role, 'm')
mat(3, 48, 24, 22, ['2', '0', '0', '1'], 'sujet')
mat(61, 48, 24, 22, ['3', '1', '1', '3'], 'varie')
arrow(ax, (28, 59), (60, 59), 'varie')
text(ax, 44, 64, 'autre base', 'varie', 's')
text(ax, 15, 42, r'$\det=2$', 'sujet', 'm')
text(ax, 73, 42, r'$\det=8$', 'varie', 'm')
u = 4.2
for j in range(2):
    box(ax, 12, 22 + j * u, u, u, 'sujet', r=0.2, lw=0.6)
for i in range(4):
    for j in range(2):
        box(ax, 50 + i * (u + 1.2), 22 + j * u, u, u, 'varie', r=0.2, lw=0.6)
text(ax, 31, 26, r'$\times\,4=2^2$', 'varie', 'm')
text(ax, 44, 8, r'$8=2\times 2^2$ : même discriminant', 'resultat', 's')
save(fig, '71-069')
