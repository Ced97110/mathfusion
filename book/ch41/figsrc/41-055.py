import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
k = 5.0
O = (12, 8)
v = (3, 4)
d = (6, 8)
assert math.hypot(*v) == 5 and math.hypot(*d) == 10
T = lambda q: (O[0] + k * q[0], O[1] + k * q[1])
line(ax, [O, (O[0] + 40, O[1])], 'fixe', lw=0.5)
line(ax, [O, (O[0], O[1] + 56)], 'fixe', lw=0.5)
for q in (v, d):
    line(ax, [T(q), (T(q)[0], O[1])], 'fixe', lw=0.5, dash=True)
    line(ax, [T(q), (O[0], T(q)[1])], 'fixe', lw=0.5, dash=True)
    text(ax, T(q)[0], O[1] - 3, '%d' % q[0], 'fixe', 's')
    text(ax, O[0] - 3, T(q)[1], '%d' % q[1], 'fixe', 's')
arrow(ax, O, T(d), 'resultat', lw=1.2)
arrow(ax, O, T(v), 'sujet', lw=2.2)
text(ax, T(v)[0] + 3, T(v)[1] - 4, r'$v$ : norme 5', 'sujet', 's', ha='left')
text(ax, T(d)[0] + 3, T(d)[1] - 1, r'$2v$ : norme 10', 'resultat', 's', ha='left')
text(ax, 44, 4, '', 'fixe', 's')
save(fig, '41-055')
