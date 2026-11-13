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
fig, ax = canvas(60)
text(ax, 44, 54, r'$\sin B = b\sin A\,/\,a$', 'sujet', 'l')
f = numberline(ax, 8, 78, 30, 0, 1.4, 0.2, arrow_right=False)
line(ax, [(f(0), 34), (f(1), 34)], 'resultat', lw=2.5); line(ax, [(f(1), 34), (f(1.4), 34)], 'limite', lw=2.5)
text(ax, f(0.5), 39, 'candidats B', 'resultat', 's'); text(ax, f(1.2), 39, 'aucun', 'limite', 's'); text(ax, f(1), 44, 'B = 90°', 'sujet', 's')
disc(ax, f(0.6662), 30, 1.3, 'resultat'); disc(ax, f(1.073), 30, 1.3, 'limite')
line(ax, [(f(0.6662), 28.5), (f(0.6662), 21)], 'resultat', dash=True); line(ax, [(f(1.073), 28.5), (f(1.073), 14.5)], 'limite', dash=True)
text(ax, f(0.6662) - 6, 20, 'a = 16,1 : 0,6662', 'resultat', 's'); text(ax, f(1.073) - 5, 13.5, 'a = 10 : 1,073', 'limite', 's')
save(fig, '36-118')
