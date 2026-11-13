import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(88)
line(ax, [(10, 78), (78, 78)], 'sujet', lw=2.0)
line(ax, [(10, 76), (10, 80)], 'sujet'); line(ax, [(78, 76), (78, 80)], 'sujet')
text(ax, 44, 84, '5 000 m', 'sujet', 'l')
text(ax, 44, 72, '5 km', 'autre', 'l')
text(ax, 44, 63, 'même longueur', 'resultat', 'm')
V = (14, 12)
line(ax, [V, (60, 12)], 'fixe', lw=1.4)
line(ax, [V, pol(V, 40, 46)], 'fixe', lw=1.4)
arc(ax, V, 0, 40, 13, 'sujet', lw=1.6)
text(ax, 44, 52, 'même angle', 'resultat', 'm')
text(ax, 62, 33, 'en degrés : 40', 'sujet', 'm', ha='left')
text(ax, 62, 25, 'en radians :', 'autre', 'm', ha='left')
text(ax, 62, 19.5, 'un autre nombre', 'autre', 's', ha='left')
save(fig, '25-026')
