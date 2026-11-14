import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 67, r'$6-6+3-1=2$', 'resultat', 'xl')
def tri(cx, cy, order, role):
    R = 14
    P = {1: (cx, cy + R), 2: (cx + R * 0.866, cy - R / 2), 3: (cx - R * 0.866, cy - R / 2)}
    for a, b in zip(order, order[1:] + order[:1]):
        (xa, ya), (xb, yb) = P[a], P[b]; d = math.hypot(xb - xa, yb - ya); ux, uy = (xb - xa) / d, (yb - ya) / d
        arrow(ax, (xa + ux * 5, ya + uy * 5), (xb - ux * 5, yb - uy * 5), role)
    for k, (x, y) in P.items(): disc(ax, x, y, 4, 'sujet', label=str(k), size='m')
tri(22, 34, [1, 2, 3], 'varie'); tri(66, 34, [1, 3, 2], 'autre')
text(ax, 22, 8, 'chacun reçoit le suivant', 'varie', 's'); text(ax, 66, 8, 'chacun reçoit le précédent', 'autre', 's')
save(fig, '80-376')
