import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
def PT(p, L, a): return (p[0] + L*math.cos(math.radians(a)), p[1] + L*math.sin(math.radians(a)))
def unit(v, w):
    d = math.hypot(w[0]-v[0], w[1]-v[1]); return ((w[0]-v[0])/d, (w[1]-v[1])/d)
def angtxt(ax, v, p1, p2, s, role, d=7.0, size='s'):
    u1, u2 = unit(v, p1), unit(v, p2); m = (u1[0]+u2[0], u1[1]+u2[1]); n = math.hypot(*m)
    text(ax, v[0]+d*m[0]/n, v[1]+d*m[1]/n, s, role, size)
def arcang(ax, v, p1, p2, r, role, lw=0.8):
    a1 = math.degrees(math.atan2(p1[1]-v[1], p1[0]-v[0])); a2 = math.degrees(math.atan2(p2[1]-v[1], p2[0]-v[0]))
    dl = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + dl) if dl > 0 else (a1 + dl, a1)
    ax.add_patch(Arc(v, 2*r, 2*r, theta1=t1, theta2=t2, color=COL[role], lw=lw, zorder=3))
def sidetxt(ax, p, q, c, s, role, d=3.6, size='s'):
    mx, my = (p[0]+q[0])/2, (p[1]+q[1])/2; nx, ny = -(q[1]-p[1]), q[0]-p[0]; L = math.hypot(nx, ny); nx, ny = nx/L, ny/L
    if (mx-c[0])*nx + (my-c[1])*ny < 0: nx, ny = -nx, -ny
    text(ax, mx+d*nx, my+d*ny, s, role, size)
fig, ax = canvas(84)
box(ax, 6, 72, 76, 9, 'varie', label=r'$h = 18{,}7 \times \sin 35° \approx 10{,}73$')
arrow(ax, (44, 72), (44, 68), 'fixe')
f = numberline(ax, 8, 76, 52, 0, 20, 5, arrow_right=False)
for v, role, lab, hh in ((10.73, 'sujet', 'h = 10,73', 6), (16.1, 'autre', 'a = 16,1', 6), (18.7, 'fixe', 'b = 18,7', 11)):
    disc(ax, f(v), 52, 1.2, role); line(ax, [(f(v), 53.2), (f(v), 52 + hh - 1.5)], role, dash=True); text(ax, f(v), 52 + hh, lab, role, 's')
text(ax, 28, 63, r'$h < a < b$ : deux triangles', 'resultat', 's')
arrow(ax, (44, 42), (44, 38), 'fixe')
box(ax, 6, 29, 76, 9, 'varie', label=r'$\sin B = 10{,}73 / 16{,}1 \approx 0{,}6662$')
arrow(ax, (44, 29), (44, 25), 'fixe')
box(ax, 6, 14, 76, 11, 'resultat', label=r'$B \approx 41{,}77°$ ou $138{,}23°$')
save(fig, '36-108')
