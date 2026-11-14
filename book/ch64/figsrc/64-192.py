import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# two chains of subgroup orders of Z/60 (orders read from the card)
left = (20, 4, 2)
right = (30, 15, 3)
assert 60 // 20 == 3 and 20 // 4 == 5 and 4 // 2 == 2 and 2 // 1 == 2
assert 60 // 30 == 2 and 30 // 15 == 2 and 15 // 3 == 5 and 3 // 1 == 3
ys = (74, 58, 42, 26, 10)
xm, xl, xr, r = 44, 18, 70, 4.6
text(ax, xl, 86, 'première suite', 'sujet', 'm', weight='bold')
text(ax, xr, 86, 'seconde suite', 'autre', 'm', weight='bold')

def edge(p, q, role):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + r * ux, p[1] + r * uy), (q[0] - r * ux, q[1] - r * uy), role, lw=0.9)

pts_l = [(xm, ys[0])] + [(xl, y) for y in ys[1:4]] + [(xm, ys[4])]
pts_r = [(xm, ys[0])] + [(xr, y) for y in ys[1:4]] + [(xm, ys[4])]
for a, b in zip(pts_l[:-1], pts_l[1:]): edge(a, b, 'sujet')
for a, b in zip(pts_r[:-1], pts_r[1:]): edge(a, b, 'autre')
disc(ax, xm, ys[0], r, 'fixe', label='60', size='s')
disc(ax, xm, ys[4], r, 'fixe', label='1', size='s')
for y, v in zip(ys[1:4], left): disc(ax, xl, y, r, 'sujet', label=str(v), size='s')
for y, v in zip(ys[1:4], right): disc(ax, xr, y, r, 'autre', label=str(v), size='s')
text(ax, xl, 2.5, 'facteurs 3, 5, 2, 2', 'sujet', 's')
text(ax, xr, 2.5, 'facteurs 2, 2, 5, 3', 'autre', 's')
save(fig, '64-192')
