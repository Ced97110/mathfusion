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

fig, ax = canvas(72)
S = nodes(ax, 16, ['1', '2', '3'], [52, 38, 24], 'sujet')
U = nodes(ax, 72, ['x'], [52], 'fixe')
disc(ax, 72, 38, R, 'limite', label='y')
disc(ax, 72, 24, R, 'resultat', label='z'); U['z'] = (72, 24)
link(ax, S['1'], U['z'], 'limite', 1.2); link(ax, S['2'], U['z'], 'limite', 1.2)
link(ax, S['3'], U['x'], 'fixe', 0.9)
text(ax, 44, 64, r'$g\circ f$ : pas bijective', 'varie', 'l')
box(ax, 2, 2, 42, 12, 'limite', label='pas injective :\n1 et 2 vont sur z', size='s')
box(ax, 46, 2, 40, 12, 'limite', label='pas surjective :\nrien n\u2019arrive en y', size='s')
save(fig, '42-275')
