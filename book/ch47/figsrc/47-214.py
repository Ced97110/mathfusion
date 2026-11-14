import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
P = {'e': (0, 0), 'a': (1, 0), 'b': (2, 0), 't': (0, 1), 'ta': (1, 1), 'tb': (2, 1)}  # b = a^2, tb = t a^2
def dots(cx, cy, groups, roles):
    pos = {k: (cx + (v[0]-1)*7, cy + (0.5 - v[1])*7) for k, v in P.items()}
    for g, r in zip(groups, roles):
        pts = [pos[k] for k in g]
        for i in range(len(pts)):
            for j in range(i+1, len(pts)): line(ax, [pts[i], pts[j]], r, lw=2.4)
        for p in pts: disc(ax, p[0], p[1], 1.8, r)
text(ax, 24, 73, 'classes à gauche', 'encre', 's'); text(ax, 66, 73, 'classes à droite', 'encre', 's')
# index 2
for cx in (24, 66):
    box(ax, cx - 13, 56.5, 26, 6, 'sujet', fill=False, r=1.5); box(ax, cx - 13, 49.5, 26, 6, 'varie', fill=False, r=1.5)
    dots(cx, 56, [['e', 'a', 'b']], ['sujet']); dots(cx, 56, [['t', 'ta', 'tb']], ['varie'])
text(ax, 44, 56, '=', 'resultat', 'xl')
for cx in (24, 66): text(ax, cx - 16, 59.5, r'$H$', 'sujet', 's'); text(ax, cx - 12, 29.5, r'$K$', 'sujet', 's')
text(ax, 44, 41, r'indice 2 : $H$ normal', 'resultat', 's')
dots(24, 22, [['e', 't'], ['a', 'tb'], ['b', 'ta']], ['sujet', 'varie', 'autre'])
dots(66, 22, [['e', 't'], ['a', 'ta'], ['b', 'tb']], ['sujet', 'varie', 'autre'])
text(ax, 44, 22, r'$\neq$', 'limite', 'xl')
text(ax, 44, 6, r'indice 3 : $K$ pas normal', 'limite', 's')
save(fig, '47-214')
