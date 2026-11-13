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

fig, ax = canvas(62)
disc(ax, 12, 40, R, 'sujet', label='1'); disc(ax, 12, 22, R, 'sujet', label='2')
disc(ax, 44, 31, R, 'varie', label='a'); disc(ax, 76, 31, R, 'resultat', label='z')
link(ax, (12, 40), (44, 31), 'varie', 1.1); link(ax, (12, 22), (44, 31), 'varie', 1.1)
link(ax, (44, 31), (76, 31), 'varie', 1.1)
text(ax, 25, 41, r'$f$', 'varie', 'l'); text(ax, 60, 35, r'$g$', 'varie', 'l')
text(ax, 12, 49, r'$1\neq 2$', 'sujet', 'm')
text(ax, 44, 20, 'même image a', 'varie', 's')
text(ax, 76, 20, 'même image z', 'resultat', 's')
brace(ax, 12, 76, 56, 'fixe', label=r'$g\circ f$ : 1 et 2 restent confondus', down=False, depth=1.4)
text(ax, 44, 7, r'$g$ ne voit qu’une valeur', 'limite', 's')
save(fig, '42-276')
