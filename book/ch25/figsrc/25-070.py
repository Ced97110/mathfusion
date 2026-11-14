import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="encre", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(54)
s = 4.5
def tri(P, rot):
    def R(v):
        x, y = v
        return (P[0] + (x if rot == 0 else -y), P[1] + (y if rot == 0 else x))
    C = R((0, 0)); A = R((4 * s, 0)); B = R((0, 3 * s))
    poly(ax, [C, A, B], 'fixe')
    line(ax, [C, A], 'sujet', lw=2.2); line(ax, [C, B], 'varie', lw=2.2); line(ax, [A, B], 'fixe', lw=2.2)
    return C, A, B
C, A, B = tri((14, 14), 0)
arc(ax, A, 5, 143.13, 180); text(ax, A[0] + 3, A[1] - 2.5, 'A', 'encre', 'm', weight='bold')
text(ax, 23, 8.5, '4 adjacent', 'sujet', 's', weight='bold'); text(ax, 7.5, 20.5, '3 opposé', 'varie', 's', weight='bold')
text(ax, 25, 44, 'feuille posée', 'encre', 'm')
C2, A2, B2 = tri((62, 12), 1)
arc(ax, A2, 5, 233.13, 270); text(ax, A2[0] + 3, A2[1] + 1.5, 'A', 'encre', 'm', weight='bold')
text(ax, 75, 25, '4 adjacent', 'sujet', 's', weight='bold'); text(ax, 56, 8.5, '3 opposé', 'varie', 's', weight='bold')
text(ax, 67, 44, 'feuille tournée', 'encre', 'm')
arrow(ax, (36, 28), (46, 28), 'varie', curve=-0.3)
text(ax, 41, 33, '¼ tour', 'varie', 's')
text(ax, 44, 2.5, 'le côté garde son rôle et sa couleur', 'resultat', 's')
save(fig, '25-070')
