import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
s = 9.0
def arc(c, r, a0, a1, role):
    n = 20
    pts = [(c[0] + r * math.cos(a0 + (a1 - a0) * i / n), c[1] + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
    line(ax, pts[:-1], role, lw=0.9)
    arrow(ax, pts[-2], pts[-1], role, lw=0.9)
ang = math.atan2(2, 1)
def panel(o, first, second, r1, r2, a_from, a_to, area, rf, rs):
    P = lambda x, y: (o[0] + x * s, o[1] + y * s)
    poly(ax, [P(0, 0), P(2, 0), P(3, 2), P(1, 2)], 'resultat')
    arrow(ax, P(0, 0), P(2, 0), r1, lw=1.6)
    arrow(ax, P(0, 0), P(1, 2), r2, lw=1.6)
    arc(o, 8, a_from, a_to, 'varie')
    text(ax, P(2, 0)[0] + 3, P(2, 0)[1] - 3.5, rf, r1, 's')
    text(ax, P(1, 2)[0] - 3, P(1, 2)[1] + 3.5, rs, r2, 's')
    text(ax, P(1.5, 1)[0], P(1.5, 1)[1], area, 'resultat', 'm', weight='bold')
panel((8, 28), 0, 0, 'sujet', 'autre', 0, ang, 'aire 4', r'$u$', r'$v$')
panel((52, 28), 0, 0, 'sujet', 'autre', ang, 0, 'aire −4', r'$u$', r'$v$')
text(ax, 25, 66, 'de u vers v : sens inverse', 'varie', 's')
text(ax, 25, 61, 'des aiguilles', 'varie', 's')
text(ax, 67, 66, 'de v vers u : sens', 'varie', 's')
text(ax, 67, 61, 'des aiguilles', 'varie', 's')
box(ax, 4, 4, 38, 12, 'resultat', label=r'aire orientée : $2\times 2-0\times 1=4$', size='s')
box(ax, 48, 4, 36, 12, 'resultat', label='aire orientée : −4', size='s')
save(fig, '41-167')
