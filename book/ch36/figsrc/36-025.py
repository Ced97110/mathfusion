import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(72)
u = 4.0
text(ax, 44, 67, r'$h = a\,\sin B$', 'encre', 'l')
for x0, ang, hv, calc in [(3, 30, r'$h=5$', r'$10\times 0{,}5 = 5$'), (48, 60, r'$h\approx 8{,}66$', r'$10\times 0{,}866\approx 8{,}66$')]:
    y0 = 14
    Bp = (x0, y0); D = (x0 + 10 * u * cs(ang), y0); Cp = (D[0], y0 + 10 * u * sn(ang))
    poly(ax, [Bp, D, Cp], 'fixe')
    line(ax, [Bp, Cp], 'sujet', lw=1.6)
    line(ax, [D, Cp], 'resultat', lw=1.8)
    rmark(ax, D, 180, 90)
    arc(ax, Bp, 7, 0, ang)
    mid = ((Bp[0] + Cp[0]) / 2, (Bp[1] + Cp[1]) / 2)
    text(ax, mid[0] - 3.5 * sn(ang) - 2, mid[1] + 3.5 * cs(ang) + 1.5, r'$a=10$', 'sujet', 's')
    text(ax, D[0] + (6 if ang == 30 else 9), (y0 + Cp[1]) / 2, hv, 'resultat', 's')
    text(ax, x0 + 9, y0 - 3.5, f'$B={ang}°$'.replace('°', r'^\circ'), 'autre', 's')
    text(ax, (Bp[0] + D[0]) / 2 + 2, 5, calc, 'resultat', 's')
save(fig, '36-025')
