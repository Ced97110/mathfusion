import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
k = 2.6
O = (8, 8)
v, m, n = (2, 3), 2, 3
assert (m * v[0], m * v[1]) == (4, 6) and (n * v[0], n * v[1]) == (6, 9) and ((m + n) * v[0], (m + n) * v[1]) == (10, 15)
T = lambda q, d=(0, 0): (O[0] + k * q[0] + d[0], O[1] + k * q[1] + d[1])
off = (3.2, -2.1)
arrow(ax, T((0, 0)), T((4, 6)), 'sujet', lw=1.8)
arrow(ax, T((4, 6)), T((10, 15)), 'autre', lw=1.8)
arrow(ax, T((0, 0), off), T((10, 15), off), 'resultat', lw=1.8)
text(ax, 6, 36, r'$2v=\langle 4;\ 6\rangle$', 'sujet', 's', ha='left')
text(ax, 6, 50, r'$3v=\langle 6;\ 9\rangle$', 'autre', 's', ha='left')
text(ax, 36, 12, r'$5v=\langle 10;\ 15\rangle$', 'resultat', 's', ha='left')
box(ax, 44, 34, 42, 10, 'fixe', label=r'$(2+3)\times 2=2\times 2+3\times 2=10$', size='s')
box(ax, 44, 20, 42, 10, 'fixe', label=r'$(2+3)\times 3=2\times 3+3\times 3=15$', size='s')
save(fig, '41-066')
