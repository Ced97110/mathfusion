import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, t0, t1, role='varie', lw=1.0, dash=False):
    ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t0, theta2=t1, color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3))
def ring(ax, c, r, role='varie', lw=1.0, dash=False):
    ax.add_patch(Circle(c, r, ec=COL[role], fc='none', lw=lw, ls='--' if dash else '-', zorder=3))
def side(ax, p, q, cen, s, role='encre', d=3.2, size='s'):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2; vx, vy = mx - cen[0], my - cen[1]; n = math.hypot(vx, vy)
    text(ax, mx + d * vx / n, my + d * vy / n, s, role, size)
def inner(v, cen, k): return (v[0] + k * (cen[0] - v[0]), v[1] + k * (cen[1] - v[1]))
fig, ax = canvas(46)
k = 1.4; y0 = 20
for ox, b, ang, htxt in ((5, 10, 30, '5'), (31, 10, 50, '7,66'), (58, 20, 30, '10')):
    a = math.radians(ang); Fp = (ox + b * math.cos(a) * k, y0); Cp = (Fp[0], y0 + b * math.sin(a) * k); A = (ox, y0)
    poly(ax, [A, Fp, Cp], 'sujet'); line(ax, [A, Cp], 'sujet', 1.6); line(ax, [Fp, Cp], 'varie', 1.6)
    line(ax, [A, (Fp[0] + 2, y0)], 'fixe', 0.9); arc(ax, A, 4, 0, ang, 'fixe')
    cx = ox + 14
    text(ax, cx, 14, f'b = {b} ; A = {ang}°', 'sujet', 's'); text(ax, cx, 9.5, f'h = {htxt}'.replace('.', ','), 'varie', 's')
text(ax, 44, 40, r'$h = b\,\sin A$', 'sujet', 'xl')
save(fig, '36-082')
