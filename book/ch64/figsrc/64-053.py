import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx, cy, R = 44, 44, 24
P = lambda k, rad=R: (cx + rad * math.sin(math.radians(15 * k)), cy + rad * math.cos(math.radians(15 * k)))
for k in range(24):
    p = P(k)
    if k % 2 == 0:
        disc(ax, p[0], p[1], 1.9, 'sujet')
    else:
        disc(ax, p[0], p[1], 1.0, 'fixe')
for k in (0, 2, 4, 6, 22):
    x, y = P(k, R + 4.5)
    text(ax, x, y, str(k), 'sujet', 's')
for k in range(0, 24, 2):
    a, b = P(k), P((k + 2) % 24)
    d = math.hypot(b[0] - a[0], b[1] - a[1]); u = ((b[0] - a[0]) / d, (b[1] - a[1]) / d)
    arrow(ax, (a[0] + u[0] * 2.4, a[1] + u[1] * 2.4), (b[0] - u[0] * 2.4, b[1] - u[1] * 2.4), 'varie', lw=0.9)
text(ax, cx, cy + 3, r'$\langle2\rangle$', 'sujet', 'xl', weight='bold')
text(ax, cx, cy - 4, 'répéter +2', 'varie', 's')
text(ax, 44, 6, 'horloge 24 h : heures paires', 'encre', 's')
save(fig, '64-053')
