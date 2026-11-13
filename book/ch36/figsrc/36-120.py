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
fig, ax = canvas(58)
u = 4.0; x0 = 8
def pair(y, lab_ref, lab_x, ref_role='fixe'):
    box(ax, x0, y + 7, 10*u, 6, 'fixe', label=lab_ref, size='s'); box(ax, x0, y, 10.726*u, 6, 'sujet', label=lab_x, size='s')
    box(ax, x0 + 10*u, y, 0.726*u, 6, 'limite', r=0.3)
    line(ax, [(x0 + 10*u, y - 1), (x0 + 10*u, y + 14)], 'fixe', dash=True)
pair(38, r'$a = 10$', r'$h \approx 10{,}73$')
pair(10, '1', r'$\sin B \approx 1{,}073$')
text(ax, 56, 44.5, r'$h > a$ : aucun triangle', 'limite', 's', ha='left'); text(ax, 56, 16.5, r'$\sin B > 1$ : aucun', 'limite', 's', ha='left')
text(ax, 30, 31, r'$\Leftrightarrow$', 'varie', 'xl')
text(ax, 44, 3.5, r'$\sin B = h / a$ : même rapport', 'fixe', 's')
save(fig, '36-120')
