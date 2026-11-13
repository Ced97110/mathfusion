import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
def arc(ax, c, r, a0, a1, role, lw=1.1, head=True):
    pts = [P(c, r, a0 + (a1 - a0) * i / 40) for i in range(41)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-4], pts[-1], role, lw)

fig, ax = canvas(92)
c = (42, 48); r = 24
line(ax, [(6, 48), (80, 48)], 'fixe', lw=0.9)
text(ax, 16, 52, 'axe du miroir', 'fixe', 's')
A = (c[0] + r, c[1]); B = (c[0], c[1] + r); C = (c[0], c[1] - r)
arc(ax, c, r, 0, 88, 'varie')
arc(ax, c, r, 0, -88, 'resultat')
arrow(ax, (B[0] - 1.5, B[1] - 3), (C[0] - 1.5, C[1] + 3), 'autre', curve=0.0)
dot(ax, A, 'sujet', 1.8); dot(ax, B, 'varie', 1.8); dot(ax, C, 'resultat', 1.8)
text(ax, A[0] + 6, A[1] + 4, '(1, 0)', 'sujet', 's')
text(ax, B[0], B[1] + 5, '(0, 1)', 'varie', 's')
text(ax, C[0], C[1] - 5, '(0, −1)', 'resultat', 's')
text(ax, 66, 70, 'quart de tour', 'varie', 's')
text(ax, 66, 26, 'quart de tour inverse', 'resultat', 's')
text(ax, 31, 38, 'miroir', 'autre', 's')
text(ax, 44, 8, 'miroir, tour, miroir = tour inverse', 'encre', 's')
save(fig, '73-196')
