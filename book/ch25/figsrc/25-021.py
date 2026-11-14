import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(60)
y = 10; s = 2.4
for (x, a, b) in ((6, 3, 4), (42, 9, 12)):
    W_, H_ = b * s, a * s
    line(ax, [(x, y), (x + W_, y)], 'sujet', lw=1.6)
    line(ax, [(x + W_, y), (x + W_, y + H_)], 'varie', lw=1.6)
    line(ax, [(x, y), (x + W_, y + H_)], 'fixe', lw=1.0)
    sq(ax, (x + W_, y), 90, 1.5)
    text(ax, x + W_ + 2.6, y + H_ / 2, f'{a}', 'varie', 's')
    text(ax, x + W_ / 2, y - 3.6, f'{b}', 'sujet', 's')
arrow(ax, (14, 24), (40, 24), 'varie')
text(ax, 27, 28, r'$\times 3$', 'varie', 'm')
text(ax, 44, 56, 'tailles différentes', 'encre', 's')
text(ax, 18, 48, r'$3/4=0{,}75$', 'resultat', 'm')
text(ax, 62, 48, r'$9/12=0{,}75$', 'resultat', 'm')
text(ax, 40, 48, '=', 'resultat', 'l')
save(fig, '25-021')
