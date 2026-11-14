import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'$C$ : puissances de (1234)', 'sujet', 'm')
R = 6.5
ang = {1: 90, 2: 0, 3: -90, 4: 180}
def pos(cx, c):
    a = math.radians(ang[c]); return (cx + R * math.cos(a), 36 + R * math.sin(a))
caps = [r'$(1234)^1$', r'$(1234)^2$', r'$(1234)^3$', r'$(1234)^4$ : rien']
steps = [1, 2, 3, 0]
for i, cx in enumerate((11, 33, 55, 77)):
    for c in (1, 2, 3, 4):
        p = pos(cx, c)
        disc(ax, p[0], p[1], 2.3, 'sujet', label=str(c) if i == 0 else None, size='s')
    k = steps[i]
    for c in (1, 2, 3, 4):
        if k == 0: break
        t = (c - 1 + k) % 4 + 1
        pa, pb = pos(cx, c), pos(cx, t)
        if k == 2 and c > t: continue
        dx, dy = pb[0] - pa[0], pb[1] - pa[1]
        d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
        arrow(ax, (pa[0] + ux * 2.9, pa[1] + uy * 2.9), (pb[0] - ux * 2.9, pb[1] - uy * 2.9), 'varie', both=(k == 2))
    text(ax, cx, 20, caps[i] if i < 3 else r'$(1234)^4$', 'varie' if k else 'fixe', 's')
maps = [(2, 3, 4, 1), (3, 4, 1, 2), (4, 1, 2, 3)]
for cx, m in zip((11, 33, 55), maps):
    text(ax, cx, 11.5, r'$%d\to%d$   $%d\to%d$' % (1, m[0], 2, m[1]) + '\n' + r'$%d\to%d$   $%d\to%d$' % (3, m[2], 4, m[3]), 'varie', 's')
text(ax, 77, 11.5, 'rien ne bouge', 'fixe', 's')
text(ax, 44, 3.5, '4 éléments, tous venus de (1234)', 'sujet', 's')
save(fig, '65-079')
