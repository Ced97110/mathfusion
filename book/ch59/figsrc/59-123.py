import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
ox, oy, sx, sy = 28, 18, 11.0, 5.4
P = lambda u, v: (ox + u * sx, oy + v * sy)
for u in range(4):
    for v in range(11):
        if u <= 1 and v <= 9:
            disc(ax, *P(u, v), 1.5, 'sujet')
        else:
            ax.plot([P(u, v)[0]], [P(u, v)[1]], 'o', color=COL['fixe'], ms=2.2, zorder=2)
line(ax, [P(-0.45, -0.45), P(1.45, -0.45), P(1.45, 9.45), P(-0.45, 9.45), P(-0.45, -0.45)], 'varie', lw=1.1, dash=True)
# retour horizontal : 2 pas vers la droite = retour au départ
arrow(ax, (P(2, 0)[0], P(2, 0)[1] - 2.5), (P(0, 0)[0], P(0, 0)[1] - 2.5), 'varie', lw=1.1, curve=-0.45)
text(ax, P(1, 0)[0], oy - 11, '2 pas : retour à 0', 'varie', 's')
# retour vertical : 10 pas vers le haut = retour au départ
arrow(ax, (P(0, 10)[0] - 3, P(0, 10)[1]), (P(0, 0)[0] - 3, P(0, 0)[1] + 1), 'varie', lw=1.1, curve=0.2)
text(ax, ox - 15, P(0, 5)[1], '10 pas : retour à 0', 'varie', 's', rot=90)
text(ax, P(3.9, 0)[0], oy, 'e′₁', 'sujet', 's')
text(ax, ox, P(0, 11)[1] + 3, 'e′₂', 'sujet', 's')
text(ax, 62, 85, '20 classes : 2 × 10', 'sujet', 'm', weight='bold')
text(ax, 62, 78, 'ℤ/2 ⊕ ℤ/10', 'autre', 'm', weight='bold')
save(fig, '59-123')
