import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
N = range(10)
cubes(ax, [(i, j, k) for i in N for j in N for k in N], (14, 22), 1.3, 'sujet')
cubes(ax, [(i, j, 0) for i in N for j in N], (40, 22), 1.3, 'fixe')
cubes(ax, [(i, 0, 0) for i in N], (58, 22), 1.3, 'fixe')
cubes(ax, [(0, 0, 0)], (79, 22), 1.3, 'fixe')
xs = [14, 40, 63, 79]
noms = ['milliers', 'centaines', 'dizaines', 'unités']
vals = ['1 000 = 10 × 100', '100', '10', '1']
for x, n, v, r in zip(xs, noms, vals, ['sujet', 'fixe', 'fixe', 'fixe']):
    text(ax, x, 17, n, r, 's')
    text(ax, x, 11.5, v, r, 'm')
text(ax, 3, 54, r'4$^{\mathrm{e}}$ case : on dit « mille »', 'sujet', 's', ha='left')
text(ax, 44, 5.5, 'le 4 de 4 329 : 4 000', 'resultat', 'm')
save(fig, '01-067')
