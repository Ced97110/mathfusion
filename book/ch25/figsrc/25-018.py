import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(50)
O = (44, 12)
line(ax, [(10, 12), (78, 12)], 'sujet', lw=2.0)
line(ax, [O, (44, 38)], 'varie', lw=2.0)
sq(ax, O, 90, 4.0, 'resultat')
text(ax, 62, 7, 'côté bleu', 'sujet', 's')
text(ax, 44, 43, 'segment orange', 'varie', 's')
text(ax, 20, 31, 'angle droit (90°)', 'resultat', 's')
arrow(ax, (26, 28), (41.5, 15.5), 'resultat')
save(fig, '25-018')
