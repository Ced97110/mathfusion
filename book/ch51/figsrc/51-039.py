import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
def link(p, q, rp, rq, role='fixe'):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    line(ax, [(p[0] + ux * rp, p[1] + uy * rp), (q[0] - ux * rq, q[1] - uy * rq)], role, lw=1.0)
def tree(xs, inner_idx, name, cap):
    ly = 16; leaves = [(x, ly) for x in xs]
    i, j = inner_idx
    mid = ((leaves[i][0] + leaves[j][0]) / 2, 32)
    rest = [k for k in range(3) if k not in inner_idx][0]
    root = ((mid[0] + leaves[rest][0]) / 2, 50)
    link(root, mid, 5.5, 4.8); link(root, leaves[rest], 5.5, 3.6)
    link(mid, leaves[i], 4.8, 3.6); link(mid, leaves[j], 4.8, 3.6)
    for (x, y), s in zip(leaves, 'abc'): disc(ax, x, y, 3.6, 'sujet', label=f'${s}$', size='m')
    disc(ax, mid[0], mid[1], 4.8, 'varie', label=name, size='s')
    disc(ax, root[0], root[1], 5.5, 'resultat', label='$abc$', size='s')
    text(ax, root[0], 5, cap, 'encre', 'm')
tree([10, 22, 34], (0, 1), '$ab$', r'$(ab)c$')
tree([54, 66, 78], (1, 2), '$bc$', r'$a(bc)$')
text(ax, 44, 50, '=', 'encre', 'xl')
save(fig, '51-039')
