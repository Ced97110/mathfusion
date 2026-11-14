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
fig, ax = canvas(62)
s = 0.2333; x0 = 8
text(ax, 4, 57, r'$\Delta = p^2 - 4q = 300 - 204$', 'sujet', 'm', ha='left')
y1 = 38
box(ax, x0, y1, 96*s, 9, 'resultat', label='96', size='s'); box(ax, x0 + 96*s, y1, 204*s, 9, 'fixe', label=r'$4q = 204$', size='s')
brace(ax, x0, x0 + 300*s, y1 + 9, 'fixe', label=r'$p^2 = 300$', down=False)
text(ax, 4, 28, r'$\Delta = 4(a^2 - h^2)$ avec $a^2 = 49$, $h^2 = 25$', 'sujet', 'm', ha='left')
y2 = 13
for i in range(4): box(ax, x0 + i*24*s, y2, 24*s, 9, 'resultat', r=0.3)
text(ax, x0 + 96*s + 3, y2 + 4.5, r'$4 \times (49 - 25) = 4 \times 24 = 96$', 'resultat', 's', ha='left')
text(ax, 44, 5, 'les deux écritures donnent 96', 'resultat', 's')
save(fig, '36-113')
