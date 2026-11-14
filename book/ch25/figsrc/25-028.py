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
A = (10, 18); C = (66, 18); B = (66, 54); D = (10, 54)
poly(ax, [A, C, B], 'sujet'); poly(ax, [A, B, D], 'autre')
th = math.degrees(math.atan2(36, 56))
arc(ax, A, 0, th, 10, 'varie', lw=1.6)
arc(ax, A, th, 90, 10, 'resultat', lw=1.6)
arc(ax, B, 180 + th, 270, 10, 'resultat', lw=1.6)
O = (38, 36)
arc(ax, O, 25, 205, 7, 'varie', lw=1.4)
arrow(ax, pol(O, 198, 7), pol(O, 212, 7), 'varie', lw=1.4)
for (p, n, dx, dy) in ((A, 'A', -4, -4), (C, 'C', 4, -4), (B, 'B', 4, 4), (D, 'D', -4, 4)):
    text(ax, p[0] + dx, p[1] + dy, rf'${n}$', 'encre', 'm')
disc(ax, O[0], O[1], 1.2, 'encre'); text(ax, O[0] + 2.5, O[1] - 3.2, r'$O$', 'encre', 'm')
text(ax, 44, 9, 'demi-tour autour de O : B va sur A', 'varie', 's')
text(ax, 44, 3.5, 'coin A : orange + vert = 90°', 'encre', 's')
save(fig, '25-028')
