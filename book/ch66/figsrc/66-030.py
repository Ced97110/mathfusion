import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(68)
cx, cy, r = 32, 34, 21
disc(ax, cx, cy, r, 'fixe', fill=False)
v = [P(cx, cy, r, 60 * k) for k in range(6)]
poly(ax, [v[0], v[2], v[4]], 'autre')
for a, b in [(0, 2), (2, 4), (4, 0)]:
    p, q = v[a], v[b]; d = math.dist(p, q); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + 2.4 * ux, p[1] + 2.4 * uy), (q[0] - 2.4 * ux, q[1] - 2.4 * uy), 'autre', lw=1.2)
for k, p in enumerate(v):
    role = 'resultat' if k in (1, 5) else ('autre' if k % 2 == 0 else 'fixe')
    disc(ax, p[0], p[1], 1.7, role)
    q = P(cx, cy, r + 5, 60 * k)
    text(ax, q[0], q[1], str(6 if k == 0 else k), role, 's')
text(ax, 74, 56, r'$\varphi(6)=2$', 'resultat', 'm')
text(ax, 74, 47, '1 et 5 :\nprimitives', 'resultat', 's')
text(ax, 74, 32, r'$\zeta_6^2$ : 2, 4, 6', 'autre', 's')
text(ax, 74, 25, '3 sommets sur 6', 'autre', 's')
text(ax, 74, 17, r'$(\zeta_6^2)^3=1$', 'autre', 's')
save(fig, '66-030')
