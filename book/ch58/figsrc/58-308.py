import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 8.0; O = (24, 20)
cubes(ax, [(i, j, k) for i in range(2) for j in range(2) for k in range(2)], O, u * 0.9, 'fixe', lw=0.4)
col = ('sujet', 'varie', 'autre')
names = (r'$u_1$', r'$u_2$', r'$u_3$')
for d, r, n in zip(((1, 0, 0), (0, 1, 0), (0, 0, 1)), col, names):
    q = iso(d[0] * 2.8, d[1] * 2.8, d[2] * 2.8, O, u * 0.9)
    arrow(ax, O, q, r, lw=1.8)
    text(ax, q[0] + (3 if d[0] else -3 if d[1] else 0), q[1] + (1 if not d[2] else 3), n, r, 's')
text(ax, 24, 57, 'W contient 3 vecteurs', 'encre', 's')
text(ax, 24, 53, 'indépendants', 'encre', 's')
x0 = 52
box(ax, x0, 38, 34, 11, 'sujet', label='u₁, u₂, u₃ dans W\nindépendants', size='s')
arrow(ax, (x0 + 17, 38), (x0 + 17, 30), 'varie')
box(ax, x0, 18, 34, 11, 'resultat', label='base de ℝ³\n(dimension 3)', size='s')
arrow(ax, (x0 + 17, 18), (x0 + 17, 10), 'varie')
box(ax, x0, 0.5, 34, 9, 'resultat', label='W = ℝ³', size='m', weight='bold')
save(fig, '58-308')
