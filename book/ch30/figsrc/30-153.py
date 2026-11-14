import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P_ = math.pi
def curve(ax, f, a, b, ox, oy, sx, sy, role, lw=1.4, dash=False, n=240):
    xs = np.linspace(a, b, n); line(ax, [(ox + x * sx, oy + f(x) * sy) for x in xs], role, lw, dash)
def circ(ax, cx, cy, r, role='fixe', lw=0.9):
    t = np.linspace(0, 2 * P_, 200); line(ax, [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in t], role, lw)
def arc(ax, cx, cy, r, a0, a1, role, head=True, lw=1.0):
    t = np.linspace(math.radians(a0), math.radians(a1), 60); pts = [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in t]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw=lw)
fig, ax = canvas(66)
oy, sx, sy = 36, 5.5, 7
cases = [(15, r'$\cos x$', np.cos, '0,5403', '0,5403', True), (44, r'$\sin x$', np.sin, '0,8415', '−0,8415', False),
         (73, r'$x+1$', lambda x: x + 1, '2', '0', False)]
for ox, title, f, va, vb, even in cases:
    line(ax, [(ox - 12.5, oy), (ox + 12.5, oy)], 'fixe'); line(ax, [(ox, oy - 8), (ox, oy + 22)], 'fixe')
    curve(ax, f, -2, 2, ox, oy, sx, sy, 'sujet')
    role = 'resultat' if even else 'limite'
    line(ax, [(ox - sx, oy + f(-1) * sy), (ox + sx, oy + f(1) * sy)], role, lw=0.8, dash=True)
    disc(ax, ox - sx, oy + f(-1) * sy, 1.2, role); disc(ax, ox + sx, oy + f(1) * sy, 1.2, role)
    text(ax, ox, oy + 27, title, 'sujet', 'm')
    text(ax, ox, oy - 13, 'en 1 : ' + (va if title != r'$\sin x$' else va), 'encre', 's')
    text(ax, ox, oy - 17.5, 'en −1 : ' + vb, 'encre', 's')
    text(ax, ox, oy - 23, 'paire' if even else 'pas paire', role, 's', weight='bold')
save(fig, '30-153')
