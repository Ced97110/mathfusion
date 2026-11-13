import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def ed(ax, p, q, role, r=R, curve=0.0, dy=0.0):
    p = (p[0], p[1] + dy); q = (q[0], q[1] + dy)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r), role, curve=curve)
fig, ax = canvas(88)
xs, xt = 12, 44
y = 74
disc(ax, xs, y, R, 'sujet', label='1'); disc(ax, xt, y, R, 'sujet', label=r'$a$')
ed(ax, (xs, y), (xt, y), 'sujet', dy=1.8); ed(ax, (xt, y), (xs, y), 'varie', dy=-1.8)
text(ax, 28, y + 6, '$\\alpha$', 'sujet', 's'); text(ax, 28, y - 6, '$\\alpha^{-1}$', 'varie', 's')
text(ax, 58, y, 'inverse : application', 'varie', 's', ha='left')
y = 46
box(ax, 2, y - 5, 28, 10, 'autre', label='$\\alpha^{-1}(B)$', size='s'); box(ax, 36, y - 5, 16, 10, 'autre', label='$B$', size='s')
arrow(ax, (35, y), (31, y), 'autre')
text(ax, 58, y, 'un ensemble', 'autre', 's', ha='left')
y = 18
disc(ax, xs, y, R, 'fixe', label='1'); disc(ax, xt, y, R, 'fixe', label='1')
ed(ax, (xs, y), (xt, y), 'fixe'); text(ax, 28, y + 4, '$1_S$', 'fixe', 's')
text(ax, 58, y, 'ne change rien', 'fixe', 's', ha='left')
save(fig, '42-240')
