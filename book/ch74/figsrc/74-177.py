import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def rh(p, ang, a, s, role):
    u = (math.cos(ang), math.sin(ang)); v = (math.cos(ang + a), math.sin(ang + a))
    pts = [p, (p[0] + s*u[0], p[1] + s*u[1]), (p[0] + s*(u[0]+v[0]), p[1] + s*(u[1]+v[1])), (p[0] + s*v[0], p[1] + s*v[1])]
    poly(ax, pts, role); return pts
# the two shapes
rh((6, 40), 0, math.radians(72), 14, 'sujet')
rh((8, 12), 0, math.radians(36), 14, 'autre')
text(ax, 15, 56, 'forme A', 'sujet', 's'); text(ax, 24, 8, 'forme B', 'autre', 's')
# order 5 star of five A shapes
c = (60, 36)
for k in range(5): rh(c, math.radians(72*k + 90), math.radians(72), 15, 'sujet')
arrow(ax, (c[0] + 22, c[1] - 6), (c[0] + 22, c[1] + 8), 'varie', curve=0.6)
text(ax, 60, 8, 'ordre 5 autour d’un point', 'varie', 's')
text(ax, 60, 59, 'ne se répète jamais exactement', 'fixe', 's')
save(fig, '74-177')
