import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

R = 3.4
def nodes(ax, x, names, ys, role):
    pos = {}
    for n, y in zip(names, ys):
        disc(ax, x, y, R, role, label=n); pos[n] = (x, y)
    return pos
def link(ax, p, q, role='varie', lw=1.0, curve=0.0):
    import math
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); k = (R+0.5)/d
    arrow(ax, (p[0]+dx*k, p[1]+dy*k), (q[0]-dx*k, q[1]-dy*k), role, lw, curve)


fig, ax = canvas(66)
S = nodes(ax, 14, ['1', '2', '3'], [54, 40, 26], 'sujet')
T = nodes(ax, 44, ['a', 'b'], [54, 33], 'autre')
U = nodes(ax, 74, ['x', 'z'], [54, 40], 'fixe')
disc(ax, 74, 26, R, 'limite', label='y')
link(ax, S['1'], T['a'], 'varie', 1.2); link(ax, S['2'], T['a'], 'varie', 1.2)
link(ax, S['3'], T['b'], 'fixe', 0.8)
link(ax, T['a'], U['z'], 'fixe', 0.8); link(ax, T['b'], U['x'], 'fixe', 0.8)
box(ax, 8, 34, 12, 27, 'varie', fill=False, dash=True)
box(ax, 68, 20, 12, 12, 'limite', fill=False, dash=True)
text(ax, 74, 15.5, 'aucune flèche', 'limite', 's')
box(ax, 3, 2, 40, 9, 'varie', label=r"$f^{-1}(\{a\})=\{1,2\}$", size='s')
box(ax, 47, 2, 40, 9, 'limite', label=r"$(g\circ f)^{-1}(\{y\})=\varnothing$", size='s')
save(fig, '42-274')
