import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
f = numberline(ax, 14, 74, 10, -2, 2, arrow_right=False)
zy = 38
line(ax, [(8, zy), (80, zy)], 'fixe', lw=0.6, dash=True)
text(ax, 81, zy, 'f = 0', 'fixe', 's', ha='left')
pts = [(-2, -1), (0, 1), (1, -1), (2, 3)]
P = [(f(x), zy + 7 * v) for x, v in pts]
for px, py in P:
    line(ax, [(px, 11.2), (px, py - 2.4)], 'fixe', lw=0.5, dash=True)
for a, b in zip(P[:-1], P[1:]):
    dx, dy = b[0] - a[0], b[1] - a[1]
    d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (a[0] + 3 * ux, a[1] + 3 * uy), (b[0] - 3 * ux, b[1] - 3 * uy), 'varie', lw=1.1)
for (x, v), (px, py) in zip(pts, P):
    disc(ax, px, py, 2.4, 'sujet', label=('−' if v < 0 else '') + str(abs(v)), size='s')
text(ax, 44, 68, r'$f(x)=x^3-3x+1$', 'sujet', 'm')
text(ax, 44, 63, '3 changements de signe', 'varie', 's')
save(fig, '69-001')
