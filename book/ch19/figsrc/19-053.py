import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(60)
PL = plane(ax, 15, 14, 10, 7, (-1, 2.5), (-0.5, 5)); PR = plane(ax, 60, 14, 10, 7, (-1, 2.5), (-0.5, 5))
line(ax, [PL(-0.5, 0), PL(1.7, 4.4)], 'resultat', lw=1.3)
for p in ((0, 1), (1, 3)): disc(ax, *PL(*p), 1.7, 'sujet')
text(ax, PL(0, 1)[0] + 2.5, PL(0, 1)[1] - 3, '(0, 1)', 'sujet', 's', ha='left'); text(ax, PL(1, 3)[0] + 2.5, PL(1, 3)[1] - 3, '(1, 3)', 'sujet', 's', ha='left')
line(ax, [PR(-0.5, 0), PR(1.7, 4.4)], 'limite', lw=1.3); line(ax, [PR(-1, 1), PR(2.5, 1)], 'limite', lw=1.3)
disc(ax, *PR(0, 1), 1.7, 'sujet'); text(ax, PR(0, 1)[0] + 2.5, PR(0, 1)[1] - 3, '(0, 1)', 'sujet', 's', ha='left')
text(ax, 22, 56, 'deux points : une droite', 'resultat', 's'); text(ax, 66, 56, 'un point : deux droites', 'limite', 's')
save(fig, '19-053')
