import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(62)
P = plane(ax, 14, 14, 10, 7, (-1, 2.2), (-0.5, 5))
line(ax, [P(-0.5, 0), P(1.9, 4.8)], 'resultat', lw=1.3)
for p in ((0, 1), (1, 3)): disc(ax, *P(*p), 1.7, 'sujet')
text(ax, P(0, 1)[0] + 2.5, P(0, 1)[1] - 3, '(0, 1)', 'sujet', 's', ha='left'); text(ax, P(1, 3)[0] + 2.5, P(1, 3)[1] - 3, '(1, 3)', 'sujet', 's', ha='left')
ys = [48, 35, 22, 9]
for y, role, s, d in zip(ys, ('sujet', 'sujet', 'resultat', 'fixe'), ('1re solution : (0, 1)', '2e solution : (1, 3)', "droite tracée : on s'arrête", '3e solution : inutile'), (False, False, False, True)):
    box(ax, 50, y, 36, 9, role, fill=not d, label=s, size='s', dash=d)
for y in ys[:3]: arrow(ax, (68, y), (68, y - 4), 'varie')
save(fig, '19-054')
