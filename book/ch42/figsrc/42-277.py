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
S = nodes(ax, 14, ['1', '2', '3'], [52, 38, 24], 'sujet')
T = nodes(ax, 44, ['a', 'b'], [52, 31], 'fixe')
U = nodes(ax, 74, ['x', 'z'], [52, 38], 'fixe')
disc(ax, 74, 24, R, 'limite', fill=False, label='y')
link(ax, S['1'], T['a'], 'fixe', 0.8); link(ax, S['2'], T['a'], 'fixe', 0.8); link(ax, S['3'], T['b'], 'fixe', 0.8)
link(ax, T['a'], U['z'], 'varie', 1.2); link(ax, T['b'], U['x'], 'varie', 1.2)
text(ax, 29, 61, r'$f$ : étape ajoutée', 'fixe', 's')
text(ax, 59, 61, r'$g$', 'varie', 'l')
text(ax, 74, 15, r'$y$ : jamais atteint', 'limite', 's')
text(ax, 30, 8, r'$g$ n’atteint pas $y$ : $g\circ f$ non plus', 'limite', 's', ha='center')
save(fig, '42-277')
