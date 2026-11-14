import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(80)
C = (44, 40); r = 17
disc(ax, C[0], C[1], r, 'fixe')
line(ax, [(C[0] - r, C[1]), (C[0] + r, C[1])], 'fixe', lw=0.8)
arc(ax, C, 0, 180, r, 'sujet', lw=3)
arc(ax, C, 180, 360, r, 'varie', lw=3)
text(ax, 44, 47, '180°', 'sujet', 'l')
text(ax, 44, 33, '180°', 'varie', 'l')
text(ax, 44, 64, '1er demi-tour', 'sujet', 's')
text(ax, 44, 16, '2e demi-tour', 'varie', 's')
text(ax, 44, 7, '180° + 180° = 360°', 'resultat', 'm')
save(fig, '25-024')
