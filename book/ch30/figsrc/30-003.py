import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(66)
x0, sx, oy, sy = 14, 5.4, 10, 6.5
T = 12.4167
f = lambda t: 4 - 2.5 * math.cos(2 * math.pi * t / T)
line(ax, [(x0, oy), (x0 + 12.4 * sx + 3, oy)], 'fixe')
line(ax, [(x0, oy), (x0, oy + 7.6 * sy)], 'fixe')
yl = oy + 5 * sy
line(ax, [(x0, yl), (x0 + T * sx, yl)], 'varie', dash=True)
tc = T / (2 * math.pi) * math.acos(-0.4)
t1, t2 = tc, T - tc
gr(ax, f, x0, oy, sx, sy, 0, t1, 'sujet'); gr(ax, f, x0, oy, sx, sy, t2, T, 'sujet')
gr(ax, f, x0, oy, sx, sy, t1, t2, 'resultat', lw=2.2)
dot(ax, x0 + t1 * sx, yl, 'varie'); dot(ax, x0 + t2 * sx, yl, 'varie')
text(ax, x0 - 1.5, oy + 6.5 * sy, '6,5 m', 'sujet', 's', ha='right')
text(ax, x0 - 1.5, oy + 1.5 * sy, '1,5 m', 'sujet', 's', ha='right')
text(ax, x0 - 1.5, yl + 3, '5 m', 'varie', 's', ha='right')
text(ax, x0 + T / 2 * sx, oy + 7.6 * sy + 2.5, 'bateau : entrée possible', 'resultat', 's')
brace(ax, x0, x0 + T * sx, oy - 1.5, 'fixe', '12 h 25 min', True)
save(fig, '30-003')
