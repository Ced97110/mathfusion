import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, '8 symétries du carré', 'encre', 'l')
# each: (vertex fixed flags, links, value)
V = [(-1, -1), (1, -1), (1, 1), (-1, 1)]  # bottom-left, bottom-right, top-right, top-left
items = [
    ([0, 1, 2, 3], [], r'$4^{4}=256$'),
    ([], 'rot', r'$4^{1}=4$'),
    ([], 'rev', r'$4^{1}=4$'),
    ([], [(0, 2), (1, 3)], r'$4^{2}=16$'),
    ([0, 2], [(1, 3)], r'$4^{3}=64$'),
    ([1, 3], [(0, 2)], r'$4^{3}=64$'),
    ([], [(0, 1), (2, 3)], r'$4^{2}=16$'),
    ([], [(0, 3), (1, 2)], r'$4^{2}=16$'),
]
s = 5.0
for n, (fixed, links, val) in enumerate(items):
    cx = 11 + 22 * (n % 4); cy = 58 - 24 * (n // 4)
    P = [(cx + s * a, cy + s * b) for a, b in V]
    poly(ax, P, 'fixe', fill=False, lw=0.6)
    if links in ('rot', 'rev'):
        for i in range(4):
            p, q = (P[i], P[(i + 1) % 4]) if links == 'rot' else (P[(i + 1) % 4], P[i])
            d = ((q[0]-p[0]), (q[1]-p[1])); L = math.hypot(*d)
            a = (p[0] + d[0] * 0.25, p[1] + d[1] * 0.25); b = (p[0] + d[0] * 0.75, p[1] + d[1] * 0.75)
            arrow(ax, a, b, 'varie', lw=0.9)
    else:
        for i, j in links: line(ax, [P[i], P[j]], 'varie', lw=1.1)
    for i in range(4):
        disc(ax, P[i][0], P[i][1], 1.5, 'resultat' if i in fixed else 'varie')
    text(ax, cx, cy - 10.5, val, 'encre', 's')
text(ax, 44, 12, r'$440\div8=55$ colorations', 'resultat', 'l')
save(fig, '49-256')
