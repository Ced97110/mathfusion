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
Rr = 17; cyy = 16
for cx in (22, 66):
    ax.add_patch(Arc((cx, cyy), 2*Rr, 2*Rr, theta1=0, theta2=180, color=COL['fixe'], lw=0.9, zorder=2))
    line(ax, [(cx - Rr - 2, cyy), (cx + Rr + 2, cyy)], 'fixe')
cx = 22
line(ax, [(cx - Rr - 2, cyy + Rr/2), (cx + Rr + 2, cyy + Rr/2)], 'sujet', dash=True)
for a_ in (30, 150):
    p = PT((cx, cyy), Rr, a_); disc(ax, p[0], p[1], 1.1, 'sujet'); q = PT((cx, cyy), Rr + 4.5, a_); text(ax, q[0], q[1], f'{a_}°', 'sujet', 's')
text(ax, cx, cyy + Rr + 8, 'sinus 0,5 : 2 angles', 'sujet', 's'); text(ax, cx, cyy - 4, 'sinus = hauteur', 'sujet', 's')
cx = 66
for sgn, role, a_, lab in ((1, 'autre', 60, '0,5'), (-1, 'fixe', 120, '−0,5')):
    line(ax, [(cx + sgn*Rr/2, cyy - 1), (cx + sgn*Rr/2, cyy + Rr + 1)], role, dash=True)
    p = PT((cx, cyy), Rr, a_); disc(ax, p[0], p[1], 1.1, role); q = PT((cx, cyy), Rr + 4.5, a_); text(ax, q[0], q[1], f'{a_}°', role, 's')
    text(ax, cx + sgn*Rr/2, cyy - 4, lab, role, 's')
text(ax, cx, cyy + Rr + 8, 'cosinus 0,5 : 1 angle', 'autre', 's'); text(ax, cx, cyy - 9, 'cosinus = abscisse', 'autre', 's')
save(fig, '36-102')
