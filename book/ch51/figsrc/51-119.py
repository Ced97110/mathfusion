import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def P(cx, cy, r, k, n=6):
    a = math.radians(90 - k * 360 / n); return (cx + r * math.cos(a), cy + r * math.sin(a))
def sh(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); return (p[0] + (q[0] - p[0]) * d / L, p[1] + (q[1] - p[1]) * d / L)
def dial(cx, cy, visited, hops, curve):
    for k in range(6):
        p = P(cx, cy, 13, k)
        disc(ax, p[0], p[1], 1.1, 'resultat' if k == 0 else ('varie' if k in visited else 'fixe'))
        if k in visited: pl = P(cx, cy, 17.5, k); text(ax, pl[0], pl[1], str(k), 'resultat' if k == 0 else 'varie', 'm', weight='bold')
    for a, b in hops:
        p, q = P(cx, cy, 13, a), P(cx, cy, 13, b)
        arrow(ax, sh(p, q, 2.0), sh(q, p, 2.0), 'varie', curve=curve)
dial(22, 52, {0, 2, 4}, [(0, 2), (2, 4), (4, 0)], 0.0)
dial(66, 52, {0, 3}, [(0, 3), (3, 0)], 0.3)
text(ax, 22, 28, r'$3\times 2=0$', 'varie', 'm'); text(ax, 66, 28, r'$2\times 3=0$', 'varie', 'm')
box(ax, 4, 14, 80, 9, 'resultat', label='commutatif : même résultat', size='s')
box(ax, 4, 3, 80, 9, 'limite', label=r'non intègre : $2\neq 0$, $3\neq 0$', size='s')
save(fig, '51-119')
