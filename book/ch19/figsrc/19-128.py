import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
fig, ax = canvas(64)
def pair(c, u, k, l1, l2, prod):
    cx, cy = c
    line(ax, [(cx - k * u, cy - k * k * u), (cx + k * u, cy + k * k * u)], 'sujet', lw=1.6) if False else None
    d1 = (1, k); d2 = (k, -1); n1 = (d1[0]**2 + d1[1]**2) ** 0.5
    a = 18 / n1
    line(ax, [(cx - a * d1[0], cy - a * d1[1]), (cx + a * d1[0], cy + a * d1[1])], 'sujet', lw=1.6)
    line(ax, [(cx - a * d2[0], cy - a * d2[1]), (cx + a * d2[0], cy + a * d2[1])], 'autre', lw=1.6)
    e1 = (d1[0] / n1, d1[1] / n1); e2 = (d2[0] / n1, d2[1] / n1); s = 3.5
    poly(ax, [(cx, cy), (cx + s * e1[0], cy + s * e1[1]), (cx + s * (e1[0] + e2[0]), cy + s * (e1[1] + e2[1])), (cx + s * e2[0], cy + s * e2[1])], 'varie')
    text(ax, cx + a * d1[0] + 1, cy + a * d1[1] + 2.5, l1, 'sujet', 's', ha='right' if k == 2 else 'left', weight='bold')
    text(ax, cx + a * d2[0] + 1, cy + a * d2[1] - 3, l2, 'autre', 's', ha='right', weight='bold')
    text(ax, cx, 6, prod, 'resultat', 's', weight='bold')
pair((22, 36), 0, 2, 'pente 2', r'pente $-\frac{1}{2}$', r'$2 \times (-\frac{1}{2}) = -1$')
pair((66, 36), 0, 3, 'pente 3', r'pente $-\frac{1}{3}$', r'$3 \times (-\frac{1}{3}) = -1$')
text(ax, 44, 61, 'angle mesuré : droit', 'varie', 's')
save(fig, '19-128')
