import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
u, oy = 22, 20
for ox, first, second, c1, c2, ttl, val, vr, rad in [(10, (1, 0), (0, 1), 'sujet', 'varie', 'sens inverse des aiguilles', 'aire orientée +1', 'resultat', 0.4), (52, (0, 1), (1, 0), 'sujet', 'varie', 'sens des aiguilles', 'aire orientée −1', 'limite', -0.4)]:
    poly(ax, [(ox, oy), (ox + u, oy), (ox + u, oy + u), (ox, oy + u)], 'fixe')
    arrow(ax, (ox, oy), (ox + first[0] * u, oy + first[1] * u), c1, lw=1.4); arrow(ax, (ox, oy), (ox + second[0] * u, oy + second[1] * u), c2, lw=1.4)
    a = (ox + (0.55 * u if first[0] else 0.2 * u), oy + (0.2 * u if first[0] else 0.55 * u)); b = (ox + (0.2 * u if first[0] else 0.55 * u), oy + (0.55 * u if first[0] else 0.2 * u))
    arrow(ax, a, b, vr, lw=1.0, curve=rad)
    text(ax, ox + u / 2, oy + u + 8, ttl, vr, 's'); text(ax, ox + u / 2 + 1, oy - 12, val, vr, 's')
    for pt, lab, cc in [(first, '1re', c1), (second, '2e', c2)]:
        text(ax, ox + (u / 2 if pt[0] else -5), oy + (-4 if pt[0] else u / 2), lab, cc, 's')
save(fig, '75-016')
