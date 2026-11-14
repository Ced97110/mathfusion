import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(52)
f = numberline(ax, 8, 70, 26, 0, 12, step=1, every=4)
for i, v in enumerate((4, 8, 12), 1):
    disc(ax, f(v), 26, 2.0, 'sujet')
    text(ax, f(v), 34, rf'$C_{i}$', 'sujet', 'l')
text(ax, 44, 47, 'même lettre, numéro différent', 'encre', 's')
text(ax, 44, 8, r'le petit chiffre n’est pas $C^2$', 'limite', 's')
save(fig, '25-017')
