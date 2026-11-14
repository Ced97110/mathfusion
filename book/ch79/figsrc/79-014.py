import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
r = 3.8
N = {'60': (44, 70, 'resultat'), '12': (22, 52, 'sujet'), '20': (66, 52, 'autre'), '4': (44, 34, 'resultat'), '2': (44, 20, 'fixe'), '1': (44, 6, 'fixe')}
for a, b in [('4','12'),('4','20'),('12','60'),('20','60'),('2','4'),('1','2')]:
    (x1, y1), (x2, y2) = N[a][:2], N[b][:2]; d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    line(ax, [(x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r)], 'fixe', lw=1.0)
for k, (x, y, c) in N.items(): disc(ax, x, y, r, c, label=k, size='s')
text(ax, 50, 70, 'seul disque au-dessus', 'resultat', 's', ha='left')
line(ax, [(54, 3), (54, 36)], 'fixe', lw=0.8)
text(ax, 57, 20, 'au-dessous : 1, 2, 4', 'fixe', 's', ha='left'); text(ax, 57, 34, '4 : le plus haut', 'resultat', 's', ha='left')
save(fig, '79-014')
