import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(64)
A = (10, 10); s = 4.5
arrow(ax, A, (72, 10), 'sujet', lw=1.6)
d = pol(A, math.degrees(math.atan2(3, 4)), 74)
arrow(ax, A, d, 'fixe', lw=1.2)
for k in (1, 2, 3):
    x = A[0] + 4 * k * s
    line(ax, [(x, 10), (x, 10 + 3 * k * s)], 'varie', lw=1.4)
    sq(ax, (x, 10), 90, 1.8)
arc(ax, A, 0, math.degrees(math.atan2(3, 4)), 7, 'resultat', lw=1.4)
text(ax, 5, 6, r'$A$', 'encre', 'm')
text(ax, 40, 4, 'demi-droite bleue', 'sujet', 's')
text(ax, 31, 41, 'demi-droite noire', 'fixe', 's', rot=37)
text(ax, 20, 58, r'même angle $A$', 'resultat', 'm')
arrow(ax, (15, 54), (15.5, 15.5), 'resultat')
save(fig, '25-019')
