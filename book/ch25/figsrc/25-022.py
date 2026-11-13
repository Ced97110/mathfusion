import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pol(V, d, r): return (V[0] + r * math.cos(math.radians(d)), V[1] + r * math.sin(math.radians(d)))
def arc(ax, V, a1, a2, r, role, lw=1.1): ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=a1, theta2=a2, ec=COL[role], lw=lw, zorder=3))
def sq(ax, V, d, s, role='fixe'):
    p1 = pol(V, d, s); p3 = pol(V, d + 90, s); p2 = (p1[0] + p3[0] - V[0], p1[1] + p3[1] - V[1]); line(ax, [p1, p2, p3], role, lw=0.8)
def inl(pts, V, k):
    gx = sum(p[0] for p in pts) / 3; gy = sum(p[1] for p in pts) / 3; dx, dy = gx - V[0], gy - V[1]; n = math.hypot(dx, dy)
    return (V[0] + k * dx / n, V[1] + k * dy / n)
fig, ax = canvas(66)
A = (8, 8); u = 5.0
line(ax, [A, (72, 8)], 'sujet', lw=1.6)
line(ax, [A, (68, 8 + 0.75 * 60)], 'fixe', lw=1.0)
for v, h in ((1, 0.75), (10, 7.5)):
    x = A[0] + v * u
    line(ax, [(x, 8), (x, 8 + h * u)], 'varie', lw=1.6)
    sq(ax, (x, 8), 90, 1.4)
    text(ax, x, 3.5, f'{v}', 'sujet', 's')
text(ax, 62.5, 27, '7,5', 'varie', 's')
text(ax, 11, 19, '0,75', 'varie', 's')
text(ax, 26, 62, 'deux nouveaux points', 'encre', 's')
text(ax, 26, 55, r'$7{,}5/10=0{,}75$', 'resultat', 's')
text(ax, 26, 48, r'$0{,}75/1=0{,}75$', 'resultat', 's')
save(fig, '25-022')
