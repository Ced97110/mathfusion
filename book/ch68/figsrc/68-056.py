import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)

def bits(ax, x, y, s, roles, cw, ch=7.0, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

x, y, z = '10101', '11010', '00011'
pos = [i for i in range(5) if x[i] != z[i]]
assert pos == [0, 2, 3]
cw = 9.0
x0 = 30
ry = {'x': 58, 'y': 38, 'z': 18}
text(ax, 44, 74, r'positions où $x$ et $z$ diffèrent', 'encre', 'm', weight='bold')
for n, w, role in [('x', x, 'sujet'), ('y', y, 'autre'), ('z', z, 'sujet')]:
    text(ax, 20, ry[n] + 3.5, r'$%s$' % n, role, 'l', weight='bold')
    bits(ax, x0, ry[n], w, role, cw)
for i in pos:
    ax.add_patch(Rectangle((x0 + i * cw + 0.2, 15.5), cw - 0.4, 52.5, fill=False, ec=COL['varie'], lw=1.0, ls='--', zorder=4))
    cx = x0 + i * cw + cw / 2
    # y diffère de x (colonnes 3, 4) ou de z (colonne 1)
    if y[i] != x[i]:
        arrow(ax, (cx, 57.5), (cx, 45.5), 'varie', both=True)
    else:
        assert y[i] != z[i]
        arrow(ax, (cx, 37.5), (cx, 25.5), 'varie', both=True)
text(ax, 44, 8, r'$y$ diffère de $x$ ou de $z$', 'varie', 'm', weight='bold')
save(fig, '68-056')
