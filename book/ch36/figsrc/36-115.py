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
fig, ax = canvas(64)
text(ax, 44, 60, r'$c^2 - 7c + 12 = 0$ : $c_1 c_2 = q$', 'fixe', 'm')
s = 6.5
for i in range(4):
    for j in range(3): box(ax, 5 + s*i, 34 + s*j, s, s, 'sujet', r=0.3, lw=0.6)
text(ax, 18, 30, r'$c_2 = 4$', 'sujet', 's'); text(ax, 33, 48, r'$c_1 = 3$', 'sujet', 's', ha='left')
text(ax, 33, 39, r'$3 \times 4 = 12 = q$', 'resultat', 's', ha='left')
w = 27.33*1.8; h = 3.31*1.8
box(ax, 37.5, 12, w, h, 'resultat', r=0.3)
text(ax, 37.5 + w/2, 21, '27,33', 'resultat', 's'); text(ax, 33.5, 12 + h/2, '3,31', 'resultat', 's')
text(ax, 44, 5.5, r'$27{,}33 \times 3{,}31 \approx 90{,}46 \approx q = 90{,}48$', 'resultat', 's')
save(fig, '36-115')
