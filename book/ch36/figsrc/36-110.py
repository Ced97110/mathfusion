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
fig, ax = canvas(80)
text(ax, 44, 74, r'$c^2 - p\,c + q = 0$', 'sujet', 'xl')
arrow(ax, (26, 69), (24, 59), 'fixe'); arrow(ax, (62, 69), (64, 59), 'fixe')
box(ax, 4, 34, 38, 25, 'varie'); box(ax, 46, 34, 38, 25, 'autre')
text(ax, 23, 54, r'$p = 2b\cos A$', 'varie', 'm'); text(ax, 23, 47, r'$2 \times 18{,}7 \times 0{,}8192$', 'varie', 's'); text(ax, 23, 39, r'$\approx 30{,}64$', 'varie', 'l')
text(ax, 65, 54, r'$q = b^2 - a^2$', 'autre', 'm'); text(ax, 65, 47, r'$18{,}7^2 - 16{,}1^2$', 'autre', 's'); text(ax, 65, 39, r'$= 90{,}48$', 'autre', 'l')
arrow(ax, (23, 34), (36, 24), 'fixe'); arrow(ax, (65, 34), (52, 24), 'fixe')
box(ax, 8, 8, 72, 15, 'resultat', label=r'$c^2 - 30{,}64\,c + 90{,}48 = 0$', size='l')
save(fig, '36-110')
