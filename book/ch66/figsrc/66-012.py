import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(82)
cx, cy, r = 44, 44, 28
disc(ax, cx, cy, r, 'fixe', fill=False)
line(ax, [(8, cy), (82, cy)], 'fixe')
v = [P(cx, cy, r, 72 * i) for i in range(5)]
c = (v[1][0], cy)
line(ax, [v[1], v[4]], 'varie', lw=1.3, dash=True)
line(ax, [(cx, cy), v[1]], 'fixe'); line(ax, [(cx, cy), v[4]], 'fixe')
line(ax, [P(cx, cy, 10, 3 * i) for i in range(25)], 'varie')
text(ax, cx + 16, cy + 6.5, '72°', 'varie', 's')
for k, p in enumerate(v):
    big = k in (1, 4)
    disc(ax, p[0], p[1], 1.9 if big else 1.4, 'varie' if big else 'sujet')
    if k == 0: text(ax, p[0] + 3, p[1] + 3.5, '1', 'sujet')
    else:
        q = P(cx, cy, r + 5, 72 * k)
        text(ax, q[0], q[1], r'$\zeta^{%d}$' % k if k > 1 else r'$\zeta$', 'varie' if big else 'sujet', weight='bold' if big else 'normal')
disc(ax, c[0], c[1], 1.8, 'varie')
text(ax, c[0] + 3, cy - 4, r'$c$', 'varie')
text(ax, 44, 3, r'$\zeta$ et $\zeta^4$ : même point $c$ sur l’axe', 'varie', 's')
save(fig, '66-012')
