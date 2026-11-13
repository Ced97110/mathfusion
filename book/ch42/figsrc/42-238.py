import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def ed(ax, p, q, role, r=R, curve=0.0, dy=0.0):
    p = (p[0], p[1] + dy); q = (q[0], q[1] + dy)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r), role, curve=curve)
fig, ax = canvas(76)
text(ax, 44, 70, 'surjective : $t$ est atteint', 'resultat', 'm')
for x, t in ((2, '$t \\in T$'), (33, '$s=\\beta(t)$'), (64, '$\\alpha(s)=t$')):
    box(ax, x, 50, 22, 10, 'sujet' if x < 64 else 'resultat', label=t, size='s')
arrow(ax, (25, 55), (32, 55), 'varie'); arrow(ax, (56, 55), (63, 55), 'varie')
text(ax, 28.5, 59.5, '$\\beta$', 'varie', 's'); text(ax, 59.5, 59.5, '$\\alpha$', 'varie', 's')
text(ax, 44, 38, 'injective : $s_1 = s_2$', 'resultat', 'm')
box(ax, 2, 14, 36, 11, 'sujet', label='$\\alpha(s_1)=\\alpha(s_2)$', size='s')
box(ax, 54, 14, 32, 11, 'resultat', label='$s_1=s_2$', size='s')
arrow(ax, (39, 19.5), (53, 19.5), 'varie', lw=1.6)
text(ax, 46, 24.5, '$\\beta$', 'varie', 's'); text(ax, 46, 12, 'étape décisive', 'varie', 's')
save(fig, '42-238')
