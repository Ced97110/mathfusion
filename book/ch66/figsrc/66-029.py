import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(68)
cx, cy, r = 29, 34, 21
disc(ax, cx, cy, r, 'fixe', fill=False)
v = [P(cx, cy, r, 72 * k) for k in range(5)]
seq = [0, 2, 4, 1, 3, 0]
for a, b in zip(seq, seq[1:]):
    p, q = v[a], v[b]; d = math.dist(p, q); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + 2.4 * ux, p[1] + 2.4 * uy), (q[0] - 2.4 * ux, q[1] - 2.4 * uy), 'varie')
for k, p in enumerate(v):
    disc(ax, p[0], p[1], 1.5, 'fixe' if k == 0 else 'resultat')
    q = P(cx, cy, r + 5, 72 * k)
    text(ax, q[0] + (1 if k == 0 else 0), q[1], '1' if k == 0 else (r'$\zeta$' if k == 1 else r'$\zeta^{%d}$' % k), 'fixe' if k == 0 else 'resultat', 's')
text(ax, 72, 52, r'$\zeta^2$ : 5 pas,' + '\ntous les sommets', 'varie', 's')
text(ax, 72, 36, r'$\varphi(5)=4$', 'resultat', 'm')
text(ax, 72, 22, 'primitives :\n' + r'$\zeta,\zeta^2,\zeta^3,\zeta^4$', 'resultat', 's')
save(fig, '66-029')
