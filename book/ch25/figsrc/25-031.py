import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(94)
s = 3.2
def tri(x, y, w, h, role): poly(ax, [(x, y), (x + w, y), (x + w, y + h)], role)
rows = ((74, 'superposable', 'mêmes côtés 3, 4, 5', 'autre'),
        (44, 'semblable', 'côtés ×2 : 6, 8, 10', 'sujet'),
        (12, 'quelconque', 'aucun lien entre côtés', 'limite'))
for i, (y, n, d, role) in enumerate(rows):
    tri(6, y, 4 * s, 3 * s, 'fixe')
    if i == 0: tri(26, y, 4 * s, 3 * s, role)
    elif i == 1: tri(26, y, 8 * s, 6 * s, role)
    else: poly(ax, [(26, y), (48, y), (31, y + 13)], role)
    h = (3 * s, 6 * s, 13)[i] / 2
    text(ax, 56, y + h + 3, n, role, 'm', ha='left')
    text(ax, 56, y + h - 3, d, 'encre', 's', ha='left')
text(ax, 6, 88, 'départ : côtés 3, 4, 5', 'fixe', 's', ha='left')
save(fig, '25-031')
