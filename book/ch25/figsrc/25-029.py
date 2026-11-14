import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(70)
t = math.tan(math.radians(40))
A = (30, 38); C = (58, 38); B = (58, 38 + 28 * t)
poly(ax, [A, C, B], 'fixe'); sq(ax, C, 90, 3, 'fixe')
arc(ax, A, 0, 40, 8, 'varie', lw=1.4); arc(ax, B, 220, 270, 7, 'varie', lw=1.4)
text(ax, *inl([A, B, C], A, 13), '40°', 'varie', 's')
text(ax, *inl([A, B, C], B, 11), '50°', 'varie', 's')
text(ax, 54, 43, '90°', 'fixe', 's')
box(ax, 8, 16, 36, 8, 'fixe', label='90°')
box(ax, 44, 16, 16, 8, 'varie', label='40°')
box(ax, 60, 16, 20, 8, 'varie', label='50°')
text(ax, 44, 30, 'bout à bout', 'encre', 's')
brace(ax, 8, 80, 14, 'resultat', label='180° = un demi-tour')
save(fig, '25-029')
