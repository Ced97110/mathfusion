import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(66)
P = plane(ax, 4, 8, 10, 5.2, (0, 4.8), (0, 9.8))
poly(ax, [P(1, 3), P(4, 3), P(4, 9)], 'sujet')
line(ax, [P(1, 3), P(4, 3)], 'varie', lw=1.5); line(ax, [P(4, 3), P(4, 9)], 'varie', lw=1.5)
for p in ((1, 3), (4, 9)): disc(ax, *P(*p), 1.6, 'sujet')
text(ax, P(1, 3)[0] + 1, P(1, 3)[1] + 4, '(1, 3)', 'sujet', 's', ha='right'); text(ax, P(4, 9)[0] - 2, P(4, 9)[1] + 3, '(4, 9)', 'sujet', 's', ha='right')
text(ax, 29.5, 19.5, '3', 'varie', 'm'); text(ax, 47.5, 39, '6', 'varie', 'm', ha='left')
for y, role, s in ((46, 'varie', r'avancée : $4-1=3$'), (30, 'varie', r'montée : $9-3=6$'), (14, 'resultat', r'$m=6\div3=2$')):
    box(ax, 56, y, 30, 9, role, label=s, size='s')
for y in (46, 30): arrow(ax, (71, y), (71, y - 7), 'varie')
save(fig, '19-062')
