import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(58)
t = math.tan(math.radians(40)); b = 40
A = (8, 10); C = (A[0] + b, 10); B = (C[0], 10 + b * t)
poly(ax, [A, C, B], 'sujet')
arc(ax, A, 0, 40, 9, 'varie', lw=1.4)
arc(ax, B, 220, 270, 7, 'varie', lw=1.4)
sq(ax, C, 90, 5.5, 'fixe')
text(ax, *pol(A, 17, 21), '40° < 90°', 'varie', 's')
text(ax, B[0] + 3, B[1] - 6, '50° < 90°', 'varie', 's', ha='left')
text(ax, C[0], 5, 'angle droit : 90°', 'fixe', 's')
text(ax, 24, 52, 'aigu : plus petit que 90°', 'varie', 's')
save(fig, '25-025')
