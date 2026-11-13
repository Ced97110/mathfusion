import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(56)
t = math.tan(math.radians(40))
A = (8, 14); C = (42, 14); B = (42, 14 + 34 * t)
poly(ax, [A, C, B], 'sujet'); sq(ax, C, 90, 3, 'fixe')
arc(ax, A, 0, 40, 8, 'varie', lw=1.4); arc(ax, B, 220, 270, 7, 'resultat', lw=1.4)
text(ax, *inl([A, B, C], A, 14), '40°', 'varie', 's')
text(ax, *inl([A, B, C], B, 11), '50°', 'resultat', 's')
for (p, n, dx, dy) in ((A, 'A', -3.5, -3.5), (C, 'C', 3.5, -3.5), (B, 'B', 3.5, 3.5)):
    text(ax, p[0] + dx, p[1] + dy, rf'${n}$', 'encre', 'm')
text(ax, 69, 44, r'$A=40°$', 'varie', 'm')
text(ax, 69, 35, r'$B=90°-A$', 'sujet', 'm')
text(ax, 69, 27, r'$=90°-40°=50°$', 'resultat', 's')
text(ax, 69, 14, r'$25°$ donne $65°$', 'encre', 's')
save(fig, '25-030')
