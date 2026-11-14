import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 30; d = (14, 10); ox, oy = 22, 12
def P(i, j, k): return (ox + i*s + j*d[0], oy + k*s + j*d[1])
roles = ['sujet', 'varie', 'autre']
for v in itertools.product((0, 1), repeat=3):
    for ax_i in range(3):
        if v[ax_i] == 0:
            w2 = list(v); w2[ax_i] = 1
            line(ax, [P(*v), P(*w2)], roles[ax_i], lw=1.2)
off = {(0,0,0): (-6,-3.5), (1,0,0): (6,-3.5), (0,0,1): (-6,3.5), (1,0,1): (6,3.5),
       (0,1,0): (6,3.5), (1,1,0): (7,-2.5), (0,1,1): (0,4.5), (1,1,1): (4,4.5)}
for v in itertools.product((0, 1), repeat=3):
    x, y = P(*v); disc(ax, x, y, 1.5, 'fixe')
    el = [n for n, b in zip('abc', v) if b]
    lab = r'$\emptyset$' if not el else r'$\{' + ','.join(el) + r'\}$'
    text(ax, x + off[v][0], y + off[v][1], lab, 'encre', 's')
text(ax, 37, 6.5, '+a', 'sujet', 's'); text(ax, 65, 13, '+b', 'varie', 's'); text(ax, 17, 27, '+c', 'autre', 's')
text(ax, 44, 63, '8 coins, 12 arêtes', 'encre', 'm')
save(fig, '42-017')
