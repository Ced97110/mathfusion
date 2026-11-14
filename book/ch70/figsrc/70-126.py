import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx, oy, u = 34, 34, 10
Y = lambda k: oy + u * k
line(ax, [(cx, Y(-2.6)), (cx, Y(2.6))], 'fixe', lw=0.6)
for k in (-2, -1, 1, 2):
    line(ax, [(cx - 16, Y(k)), (cx + 18, Y(k))], 'fixe', lw=0.4, dash=True)
roles = {1: 'sujet', -1: 'sujet', 2: 'autre', -2: 'autre'}
names = {1: r'$i$', -1: r'$-i$', 2: r'$2i$', -2: r'$-2i$'}
for k in (-2, -1, 1, 2):
    disc(ax, cx, Y(k), 1.3, roles[k])
    text(ax, cx - 3, Y(k) + 2.3, names[k], roles[k], 's', ha='right')
def seg(xx, k0, k1, lab, side):
    arrow(ax, (xx, Y(k0)), (xx, Y(k1)), 'varie', lw=0.9, both=True)
    text(ax, xx + side, (Y(k0) + Y(k1)) / 2, lab, 'varie', 's')
seg(cx + 8, 1, 2, '1', 3)
seg(cx + 8, -1, -2, '1', 3)
seg(cx + 18, -1, 2, '3', 3)
seg(cx - 16, 1, -2, '3', -3)
text(ax, 4, 66, r'racines de $f$', 'sujet', 's', ha='left')
text(ax, 30, 66, r'racines de $g$', 'autre', 's', ha='left')
text(ax, 71, 45, r'$x=4$', 'encre', 'm')
box(ax, 57, 22, 29, 14, 'resultat', label='produit :\n$1\\times3\\times3\\times1=9$', size='s')
save(fig, '70-126')
