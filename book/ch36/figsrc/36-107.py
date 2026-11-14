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
fig, ax = canvas(72)
k = 2.6; A = (6, 22); C = (A[0] + 15.318*k, A[1] + 10.7259*k)
B2 = (A[0] + 27.33*k, A[1]); B1 = (A[0] + 3.31*k, A[1])
line(ax, [A, (B2[0] + 6, 22)], 'fixe')
poly(ax, [A, B2, C], 'sujet', fill=False); line(ax, [C, B1], 'autre', lw=1.2); line(ax, [A, C], 'sujet')
disc(ax, B2[0], B2[1], 1.1, 'sujet'); disc(ax, B1[0], B1[1], 1.1, 'autre'); disc(ax, C[0], C[1], 1.1, 'sujet')
text(ax, 2.8, 25, 'A', 'fixe', 's'); text(ax, C[0], C[1] + 3.5, 'C', 'sujet', 's')
text(ax, B2[0], 26, r'$B_2$', 'sujet', 's'); text(ax, B1[0] + 1.5, 26, r'$B_1$', 'autre', 's')
arcang(ax, B2, A, C, 4, 'sujet'); text(ax, B2[0] - 8, 29.5, '41,77°', 'sujet', 's')
arcang(ax, B1, A, C, 3, 'autre'); text(ax, 9, 31.5, '138,23°', 'autre', 's')
arrow(ax, (A[0], 14), (B1[0], 14), 'autre', both=True); text(ax, B1[0] + 2, 14, r'$AB_1 \approx 3{,}31$', 'autre', 's', ha='left')
arrow(ax, (A[0], 7), (B2[0], 7), 'sujet', both=True); text(ax, 44, 3.2, r'$AB_2 \approx 27{,}33$', 'sujet', 's')
text(ax, 62, 55, 'le plus loin : angle aigu', 'sujet', 's'); text(ax, 62, 50, 'le plus proche : obtus', 'autre', 's')
save(fig, '36-107')
