import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def tick(ax, C, T, s, role='varie'):
    ang = math.degrees(math.atan2(T[1] - C[1], T[0] - C[0]))
    line(ax, [P(C[0], C[1], s, ang - 9 + 18 * i / 12) for i in range(13)], role, lw=0.8, dash=True)
fig, ax = canvas(70)
cx, cy, r = 30, 36, 24
disc(ax, cx, cy, r, 'fixe', fill=False)
line(ax, [(4, cy), (60, cy)], 'fixe')
v = [P(cx, cy, r, 72 * k) for k in range(5)]
c = (v[1][0], cy)
line(ax, [(c[0], cy - 27), (c[0], cy + 27)], 'varie')
s = math.dist(v[0], v[1])
tick(ax, v[1], v[2], s); tick(ax, v[1], v[0], s); tick(ax, v[4], v[3], s)
for k, p in enumerate(v):
    disc(ax, p[0], p[1], 1.5, 'sujet' if k in (1, 4) else 'resultat')
    q = P(cx, cy, r + 5, 72 * k)
    text(ax, q[0] + (1 if k == 0 else 0), q[1] + (3 if k == 0 else 0), '1' if k == 0 else (r'$\zeta$' if k == 1 else r'$\zeta^{%d}$' % k), 'sujet' if k in (1, 4) else 'resultat')
disc(ax, c[0], c[1], 1.6, 'varie'); text(ax, c[0] + 2.5, cy - 3.5, r'$c$', 'varie')
text(ax, 72, 58, r'1. placer $c$', 'varie', 's')
text(ax, 72, 44, '2. perpendiculaire\nen $c$ : $\\zeta$, $\\zeta^4$', 'sujet', 's')
text(ax, 72, 26, '3. compas : on\nreporte le côté', 'resultat', 's')
save(fig, '66-017')
