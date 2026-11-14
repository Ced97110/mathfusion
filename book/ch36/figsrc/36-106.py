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
fig, ax = canvas(50)
k = 2.2; A = (8, 18); C = PT(A, 18.7*k, 35)
line(ax, [A, (84, 18)], 'fixe'); line(ax, [A, C], 'sujet', lw=1.6); disc(ax, C[0], C[1], 1.1, 'sujet')
r = 16.1*k
ax.add_patch(Arc(C, 2*r, 2*r, theta1=250, theta2=290, color=COL['autre'], lw=1.2, ls='--', zorder=3))
arcang(ax, A, (84, 18), C, 7, 'sujet'); text(ax, 22, 22.5, '35°', 'sujet', 's')
text(ax, 20, 36, 'b = 18,7', 'sujet', 's')
text(ax, C[0] + 4, 3.5, 'a = 16,1 : en face de A', 'autre', 's', ha='left')
text(ax, 66, 21.5, 'droite du troisième côté', 'fixe', 's')
save(fig, '36-106')
