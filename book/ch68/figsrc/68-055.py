import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

def d(a, b):
    return sum(p != q for p, q in zip(a, b))

x, y, z = '000', '100', '111'
assert (d(x, y), d(y, z), d(x, z)) == (1, 2, 3)
cw = 5.5
xs = [4, 36, 68.5]
ys = 24
bits(ax, xs[0], ys, x, 'sujet', cw)
bits(ax, xs[1], ys, y, ['varie'] + ['autre'] * 2, cw)
bits(ax, xs[2], ys, z, 'sujet', cw)
for xx, n in zip(xs, 'xyz'):
    text(ax, xx + 1.5 * cw, ys - 4.5, r'$%s$' % n, 'encre', 'm', weight='bold')
# détour par y
arrow(ax, (xs[0] + 3 * cw + 1, ys + 3.25), (xs[1] - 1, ys + 3.25), 'varie')
arrow(ax, (xs[1] + 3 * cw + 1, ys + 3.25), (xs[2] - 1, ys + 3.25), 'varie')
text(ax, (xs[0] + 3 * cw + xs[1]) / 2, ys + 10, '1', 'varie', 'm', weight='bold')
text(ax, (xs[1] + 3 * cw + xs[2]) / 2, ys + 10, '2', 'varie', 'm', weight='bold')
# trajet direct
arrow(ax, (xs[0] + 1.5 * cw, ys + 8), (xs[2] + 1.5 * cw, ys + 8), 'sujet', curve=-0.35, lw=1.4)
text(ax, 44, 54, '3', 'sujet', 'l', weight='bold')
text(ax, 44, 8, r'$d(x, z) = 3 \leq d(x, y) + d(y, z) = 1 + 2$', 'encre', 'm')
save(fig, '68-055')
