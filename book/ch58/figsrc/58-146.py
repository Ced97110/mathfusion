import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u, O = 9.0, (78, 18)
P = lambda p: (O[0] + p[0] * u, O[1] + p[1] * u)
vs = [(3, 1), (1, 2), (-1, 3)]
cs = [-1, 2, -1]
steps = [(c * v[0], c * v[1]) for c, v in zip(cs, vs)]
pts = [(0, 0)]
for s in steps:
    pts.append((pts[-1][0] + s[0], pts[-1][1] + s[1]))
assert pts[-1] == (0, 0) and pts[1] == (-3, -1) and pts[2] == (-1, 3)
roles = ['sujet', 'autre', 'varie']
for k in range(3):
    arrow(ax, P(pts[k]), P(pts[k + 1]), roles[k], lw=1.5)
disc(ax, *P((0, 0)), 1.3, 'resultat')
text(ax, P((0, 0))[0] - 2, P((0, 0))[1] - 4, r'$(0,0)$', 'resultat', 's', ha='right')
text(ax, 2, 58, 'trois pas à la suite :', 'fixe', 's', ha='left')
text(ax, 2, 48, r'$-1\times(3,1)$', 'sujet', 'm', ha='left')
text(ax, 2, 38, r'$2\times(1,2)$', 'autre', 'm', ha='left')
text(ax, 2, 28, r'$-1\times(-1,3)$', 'varie', 'm', ha='left')
text(ax, 2, 16, 'retour au départ :', 'resultat', 's', ha='left')
text(ax, 2, 11, 'vecteur nul', 'resultat', 's', ha='left')
save(fig, '58-146')
