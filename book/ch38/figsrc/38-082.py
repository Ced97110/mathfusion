import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def sommet(a, b, base, A):
    """Sommet de la visée de A (angle a) et de la visée de B (angle intérieur b)."""
    ap = 180 - a - b
    d = base * math.sin(math.radians(b)) / math.sin(math.radians(ap))
    return (A[0] + d * math.cos(math.radians(a)), A[1] + d * math.sin(math.radians(a)))

fig, ax = canvas(92)
base = 18.0
panels = [  # (y du bord, rôle, angle A, angle B, erreur sur B, noms)
    (56, 'resultat', 60, 60, 3, ('S', "S'")),
    (12, 'autre', 12, 162, -3, ('T', "T'")),
]
for g, role, a, b, e, (n1, n2) in panels:
    A = (6.0, g); B = (A[0] + base, g)
    S = sommet(a, b, base, A); S2 = sommet(a, b + e, base, A)
    poly(ax, [A, B, S], role)
    line(ax, [A, S2], role, dash=False)
    # visée faussée depuis B (tirets) jusqu'au nouveau sommet
    line(ax, [B, S2], 'varie', lw=1.1, dash=True)
    disc(ax, S[0], S[1], 0.9, role); disc(ax, S2[0], S2[1], 0.9, 'varie')
    disc(ax, A[0], A[1], 0.9, 'encre'); disc(ax, B[0], B[1], 0.9, 'encre')
    text(ax, A[0] - 2.5, g - 3, 'A', 'encre', 's'); text(ax, B[0] + 1.5, g - 3, 'B', 'encre', 's')
    text(ax, S[0], S[1] + 3.2, n1, role, 's')
    text(ax, S2[0] + 3.5, S2[1] + 3.2, n2, 'varie', 's')
text(ax, 62, 66, 'angle entre visées : 60°', 'resultat', 's')
text(ax, 62, 5, 'angle entre visées : 6°', 'autre', 's')
text(ax, 44, 88, 'même base, même erreur de 3° en B', 'encre', 'm')
save(fig, '38-082')
