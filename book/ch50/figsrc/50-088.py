import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
c30 = math.cos(math.radians(30))
xs = [14, 44, 74]; cy, R = 28, 8
V = lambda cx, k: {'A': (cx, cy + R), 'B': (cx - R * c30, cy - R / 2), 'C': (cx + R * c30, cy - R / 2)}[k]
for k, cx in zip('ABC', xs):
    poly(ax, [V(cx, q) for q in 'ABC'], 'fixe')
    v = V(cx, k); d = ((cx - v[0]) / R, (cy - v[1]) / R)
    line(ax, [(v[0] - d[0], v[1] - d[1]), (v[0] + d[0] * (1.5 * R + 1), v[1] + d[1] * (1.5 * R + 1))], 'varie', lw=1.1, dash=True)
    off = {'A': (0, 3.6), 'B': (-3, -2.5), 'C': (3, -2.5)}[k]
    text(ax, v[0] + off[0], v[1] + off[1], k, 'sujet', 's', weight='bold')
    text(ax, cx, 11, r'$P_%s$' % k, 'sujet', 'm')
for a, b in ((14, 44), (44, 74)):
    arrow(ax, (a + 11, cy), (b - 11, cy), 'varie', lw=1.2)
    text(ax, (a + b) / 2, cy + 3.2, r'$r$', 'varie', 's')
arrow(ax, (74, 42), (14, 42), 'varie', lw=1.2, curve=0.25)
text(ax, 44, 55, r'$r$', 'varie', 's')
text(ax, 44, 3, r'$rP_Ar^{-1} = P_B$', 'encre', 's')
save(fig, '50-088')
