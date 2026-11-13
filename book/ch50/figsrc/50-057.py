import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
r = 1.5
def short(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / L, (q[1] - p[1]) / L)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
def cycle(cx, cy, n, R):
    pts = [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]
    for k in range(n):
        p, q = short(pts[k], pts[(k + 1) % n], r + 0.5); arrow(ax, p, q, 'varie', lw=0.9)
    for p in pts: disc(ax, *p, r, 'sujet')
text(ax, 44, 70, r'$60 = 2^2 \times 3 \times 5$', 'encre', 'm')
CY = 40.0
# ordre 2 : deux échanges
for dy in (-6.5, 6.5):
    a, b = (14.0 - 7, CY + dy), (14.0 + 7, CY + dy)
    p, q = short(a, b, r + 0.5)
    arrow(ax, p, q, 'varie', lw=0.9, both=True)
    disc(ax, *a, r, 'sujet'); disc(ax, *b, r, 'sujet')
cycle(44.0, CY, 3, 9.5)
cycle(72.0, CY, 5, 11.0)
for x, o, p in ((15.0, 2, r'$(1\ 2)(3\ 4)$'), (44.0, 3, r'$(1\ 2\ 3)$'), (72.0, 5, r'$(1\ 2\ 3\ 4\ 5)$')):
    text(ax, x, 60, f'ordre {o}', 'sujet', 's')
    text(ax, x, 19, p, 'encre', 's')
save(fig, '50-057')
