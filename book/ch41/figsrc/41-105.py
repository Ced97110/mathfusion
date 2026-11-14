import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u, v, w = (2, 0, 0), (1, 2, 0), (0, 0, 4)
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
assert dot(u, w) == 0 and dot(v, w) == 0
o = (22, 6); s = 7
I = lambda p: iso(p[0], p[1], p[2], o, s)
fig, ax = canvas(56)

def square(a, b, t):
    p = [(0, 0, 0), tuple(x * t for x in a), tuple(x * t + y * t for x, y in zip(a, b)), tuple(y * t for y in b)]
    line(ax, [I(p[1]), I(p[2]), I(p[3])], 'fixe')

arrow(ax, I((0, 0, 0)), I(u), 'sujet', lw=1.2)
arrow(ax, I((0, 0, 0)), I(v), 'autre', lw=1.2)
arrow(ax, I((0, 0, 0)), I(w), 'resultat', lw=1.8)
square((1, 0, 0), (0, 0, 1), 0.45)
n = 5 ** 0.5
square((1 / n, 2 / n, 0), (0, 0, 1), 0.45)
text(ax, I(u)[0] + 2, I(u)[1] - 3, r'$u$', 'sujet', ha='left')
text(ax, I(v)[0] - 2, I(v)[1] + 2, r'$v$', 'autre', ha='right')
text(ax, I(w)[0] + 4, I(w)[1], r'$u\times v$', 'resultat', ha='left')
text(ax, 66, 40, r'$u\cdot(u\times v)$', 'sujet', 's')
text(ax, 66, 35, r'$2\times0+0\times0+0\times4=0$', 'sujet', 's')
text(ax, 66, 24, r'$v\cdot(u\times v)$', 'autre', 's')
text(ax, 66, 19, r'$1\times0+2\times0+0\times4=0$', 'autre', 's')
text(ax, 66, 10, 'deux angles droits', 'encre', 's')
save(fig, '41-105')
