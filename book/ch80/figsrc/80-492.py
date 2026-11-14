import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def seg(ax, a, b, r, role='fixe'):
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    line(ax, [(a[0]+u[0]*r, a[1]+u[1]*r), (b[0]-u[0]*r, b[1]-u[1]*r)], role)
P = {1: (44, 8), 2: (28, 26), 3: (60, 26), 4: (12, 44), 6: (44, 44), 12: (28, 62)}
for a, b in [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)]: seg(ax, P[a], P[b], 6.2)
for k, (x, y) in P.items(): disc(ax, x, y, 6.2, 'sujet', label=f'{k}\n$\\langle {12 // k}\\rangle$', size='s')
text(ax, 86, 68, 'sous-groupes de l’horloge\nrangés comme les diviseurs\nde 12', 'fixe', 's', ha='right')
text(ax, 86, 12, '$k$ : nombre de pas\navant de revenir à 0\n$\\langle g\\rangle$ : sous-groupe\nengendré par le pas $g$', 'varie', 's', ha='right')
save(fig, '80-492')
