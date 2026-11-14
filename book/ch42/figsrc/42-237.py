import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def ed(ax, p, q, role, r=R, curve=0.0, dy=0.0):
    p = (p[0], p[1] + dy); q = (q[0], q[1] + dy)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r), role, curve=curve)
fig, ax = canvas(96)
xl, xr = 20, 60
top = [84, 72, 60]; bot = [34, 22, 10]
dots(ax, xl, ['1', '2', '3'], top, 'sujet'); dots(ax, xr, [r'$a$', r'$b$', r'$c$'], top, 'sujet')
for y in top: ed(ax, (xl, y), (xr, y), 'sujet')
text(ax, 40, 90, '$\\alpha$', 'sujet', 'm')
dots(ax, xl, ['1', '2', '3'], bot, 'fixe'); dots(ax, xr, [r'$a$', r'$b$', r'$c$'], bot, 'fixe')
for y in bot: ed(ax, (xr, y), (xl, y), 'varie')
text(ax, 40, 40, '$\\beta$', 'varie', 'm')
text(ax, 80, 72, '1 flèche', 'sujet', 's') if False else None
save(fig, '42-237')
