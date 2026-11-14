import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def ed(ax, p, q, role, r=R, curve=0.0, dy=0.0):
    p = (p[0], p[1] + dy); q = (q[0], q[1] + dy)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r), role, curve=curve)
fig, ax = canvas(80)
xs, xt = 16, 56; ys = [58, 44, 30]
text(ax, xs, 72, '$S$', 'sujet', 'l'); text(ax, xt, 72, '$T$', 'sujet', 'l')
dots(ax, xs, ['1', '2', '3'], ys, 'sujet'); dots(ax, xt, [r'$a$', r'$b$', r'$c$'], ys, 'sujet')
for y in ys:
    ed(ax, (xs, y), (xt, y), 'sujet', dy=1.3); ed(ax, (xt, y), (xs, y), 'varie', dy=-1.3)
text(ax, 36, 63, '$\\alpha$', 'sujet', 'm'); text(ax, 36, 25, '$\\beta$', 'varie', 'm')
text(ax, 72, 58, '$\\beta\\circ\\alpha = 1_S$', 'resultat', 's') if False else None
text(ax, 44, 14, '$\\beta \\circ \\alpha = 1_S$', 'resultat', 'm'); text(ax, 44, 5, '$\\alpha \\circ \\beta = 1_T$', 'resultat', 'm')
save(fig, '42-236')
