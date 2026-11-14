import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# trois familles de deux vecteurs et l'aire du parallélogramme qu'elles bordent
panels = [
    ([(1, 0), (0, 1)], 'sujet', 'aire 1', '(1, 0), (0, 1)', 'tout le réseau'),
    ([(2, 1), (1, 1)], 'sujet', 'aire 1', '(2, 1), (1, 1)', 'tout le réseau'),
    ([(2, 0), (0, 1)], 'autre', 'aire 2', '(2, 0), (0, 1)', 'une partie du réseau'),
]
u = 7.0
for k, (vecs, role, a, v, d) in enumerate(panels):
    ox, oy = 4 + 28.5 * k, 26
    for i in range(4):
        for j in range(3):
            disc(ax, ox + i * u, oy + j * u, 0.55, 'fixe')
    (p, q), (r_, s) = vecs
    pts = [(ox, oy), (ox + p * u, oy + q * u), (ox + (p + r_) * u, oy + (q + s) * u), (ox + r_ * u, oy + s * u)]
    poly(ax, pts, role)
    arrow(ax, pts[0], pts[1], role, lw=1.4)
    arrow(ax, pts[0], pts[3], role, lw=1.4)
    cx = ox + 1.5 * u
    text(ax, cx, 51, a, role, 'm', weight='bold')
    text(ax, cx, 14, v, role, 's')
    text(ax, cx, 8, d, role, 's')
save(fig, '58-343')
