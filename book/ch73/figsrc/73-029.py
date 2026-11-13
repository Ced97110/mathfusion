import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
u = 8.5
def dot(x, y, role):
    ax.add_patch(Circle((x, y), 1.0, fc=COL[role], ec=COL[role], zorder=6))
c, s = math.cos(math.radians(30)), math.sin(math.radians(30))
mats = [('rotation : det 1', ((c, -s), (s, c))),
        ('dilatation : det 2', ((2, 0), (0, 1))),
        ('réflexion : det −1', ((-1, 0), (0, 1))),
        ('cisaillement : det 1', ((1, 1), (0, 1)))]
text(ax, 44, 91.5, r'$GL_2(\mathbb{R})$ : quatre transformations', 'sujet', 's')
text(ax, 44, 86.5, 'bleu avant, vert après : O fixe', 'encre', 's')
for k, (name, M) in enumerate(mats):
    px, py = 2 + 44 * (k % 2), 44 - 38 * (k // 2)
    ox, oy = px + 22 - (3 if k == 2 else 0) , py + 17
    T = lambda p: (ox + (M[0][0] * p[0] + M[0][1] * p[1]) * u, oy + (M[1][0] * p[0] + M[1][1] * p[1]) * u)
    line(ax, [(ox - 1.5 * u, oy), (ox + 2.3 * u, oy)], 'fixe', lw=0.4)
    sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
    poly(ax, [T(p) for p in sq], 'resultat')
    poly(ax, [(ox + a * u, oy + b * u) for a, b in sq], 'sujet', fill=False, lw=0.7)
    line(ax, [(ox, oy - 1.0 * u), (ox, oy + 1.9 * u)], 'sujet', lw=2.2)
    line(ax, [T((0, -1.0)), T((0, 1.9))], 'resultat', lw=1.0)
    dot(ox, oy, 'encre')
    if k == 0: text(ax, ox - 3, oy - 2.8, 'O', 'encre', 's')
    text(ax, px + 22, py - 2.5, name, 'encre', 's')
save(fig, '73-029')
