import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def ed(ax, p, q, role, r=R, curve=0.0, dy=0.0):
    p = (p[0], p[1] + dy); q = (q[0], q[1] + dy)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r), role, curve=curve)
fig, ax = canvas(80)
xs, xt = 14, 50; ys = [56, 28]; yt = [66, 46, 26]
text(ax, xs, 76, '$S$', 'sujet', 'l'); text(ax, xt, 76, '$T$', 'sujet', 'l')
dots(ax, xs, ['1', '2'], ys, 'sujet')
for L, y, r in zip((r'$a$', r'$b$', r'$c$'), yt, ('sujet', 'limite', 'sujet')): disc(ax, xt, y, R, r, label=L)
ed(ax, (xs, ys[0]), (xt, yt[0]), 'sujet'); ed(ax, (xs, ys[1]), (xt, yt[2]), 'sujet')
ed(ax, (xt, yt[0]), (xs, ys[0]), 'varie', curve=0.3); ed(ax, (xt, yt[1]), (xs, ys[0]), 'varie')
ed(ax, (xt, yt[2]), (xs, ys[1]), 'varie', curve=0.3)
text(ax, 77, 56, '$\\beta\\circ\\alpha=1_S$', 'resultat', 's'); text(ax, 77, 46, 'vrai', 'resultat', 's')
text(ax, 77, 36, '$\\alpha\\circ\\beta\\neq 1_T$', 'limite', 's'); text(ax, 77, 26, '$b \\to 1 \\to a$', 'limite', 's')
text(ax, 28, 70, '$\\alpha$', 'sujet', 's') if False else None
save(fig, '42-239')
