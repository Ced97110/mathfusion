import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
th = math.radians(35); u = 16
c, s, t, ct = math.cos(th), math.sin(th), math.tan(th), 1 / math.tan(th)
def rt(ox, oy, a, b, c3, thick):
    # O=a-corner. pts: O, A (on axis), P ; thick = index of side drawn as radius (0:OA,1:AP,2:OP)
    pts = [(ox, oy), a, b]
    poly(ax, pts, 'fixe')
    sides = [(pts[0], pts[1]), (pts[1], pts[2]), (pts[0], pts[2])]
    for i, (p, q) in enumerate(sides):
        line(ax, [p, q], 'sujet' if i == thick else 'fixe', lw=2.2 if i == thick else 0.9)
    return pts
y0 = 18
# OHP : OP = 1 (hypoténuse)
ox = 4
rt(ox, y0, (ox + c * u, y0), (ox + c * u, y0 + s * u), None, 2)
# OAT : OA = 1 (côté)
ox2 = 33
rt(ox2, y0, (ox2 + u, y0), (ox2 + u, y0 + t * u), None, 0)
# OBS : OB = 1 (côté vertical)
ox3 = 60
rt(ox3, y0, (ox3, y0 + u), (ox3 + ct * u, y0 + u), None, 0)
# rotate semantics: for OBS the radius is the vertical side OB
for (x, w) in [(4, c * u), (33, u), (60, ct * u)]:
    pass
text(ax, 4 + c * u / 2, 12, 'OHP', 'encre', 'm', weight='bold')
text(ax, 33 + u / 2, 12, 'OAT', 'encre', 'm', weight='bold')
text(ax, 60 + ct * u / 2, 12, 'OBS', 'encre', 'm', weight='bold')
text(ax, 4 + c * u * 0.35, y0 + s * u * 0.62 + 2.4, '1', 'sujet', 'm', weight='bold')
text(ax, 33 + u / 2, y0 + 2.4, '1', 'sujet', 'm', weight='bold')
text(ax, 60 - 2.2, y0 + u / 2, '1', 'sujet', 'm', weight='bold')
text(ax, 4 + c * u / 2, 7.5, 'hypoténuse', 'sujet', 's')
text(ax, 33 + u / 2, 7.5, 'côté de l’angle droit', 'sujet', 's')
text(ax, 60 + ct * u / 2, 7.5, 'côté de l’angle droit', 'sujet', 's')
text(ax, 44, 42, 'le rayon 1 change de place', 'encre', 'l')
save(fig, '31-081')
