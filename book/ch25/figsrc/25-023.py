import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(74)
for cx, role in ((22, 'sujet'), (66, 'limite')):
    disc(ax, cx, 46, 14, role)
    for d in (90, 210, 330):
        line(ax, [(cx, 46), pol((cx, 46), d, 14)], role, lw=1.1)
for d in (150, 270, 30):
    p = pol((22, 46), d, 8); text(ax, p[0], p[1], '120°', 'sujet', 's')
text(ax, 22, 66, '360°', 'sujet', 'l')
text(ax, 66, 66, '100°', 'limite', 'l')
text(ax, 22, 25, r'$360\div8=45$', 'resultat', 's')
text(ax, 22, 18, r'$360\div12=30$', 'resultat', 's')
text(ax, 66, 25, r'$100\div3=33{,}333\ldots$', 'limite', 's')
text(ax, 66, 18, 'ne tombe pas juste', 'limite', 's')
save(fig, '25-023')
