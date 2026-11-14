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
fig, ax = canvas(54)
text(ax, 44, 49, 'C = 100°, b = 4, c = 5', 'sujet', 's')
def third(B0, C0, L):
    A0 = 180 - B0 - C0; return PT((0, 0), L*math.sin(math.radians(C0))/math.sin(math.radians(A0)), B0)
Bv = (6, 14); Cv = (22, 14); t = third(51.98, 100, 16); Av = (Bv[0] + t[0], Bv[1] + t[1])
poly(ax, [Bv, Cv, Av], 'sujet'); cen = ((Bv[0]+Cv[0]+Av[0])/3, (Bv[1]+Cv[1]+Av[1])/3)
sidetxt(ax, Cv, Av, cen, 'b = 4', 'sujet', d=4.5); sidetxt(ax, Bv, Av, cen, 'c = 5', 'sujet', d=4.5)
arcang(ax, Bv, Cv, Av, 4, 'varie'); arcang(ax, Cv, Bv, Av, 3.5, 'sujet')
text(ax, 11, 10.3, '51,98°', 'varie', 's'); angtxt(ax, Cv, Bv, Av, '100°', 'sujet', d=7)
B2 = (60, 14); C2 = (76, 14); line(ax, [B2, C2], 'fixe', lw=1.1)
e1 = PT(B2, 24, 128.02); e2 = PT(C2, 24, 80)
line(ax, [B2, e1], 'limite', dash=True); line(ax, [C2, e2], 'limite', dash=True)
arcang(ax, B2, C2, e1, 4, 'limite'); arcang(ax, C2, B2, e2, 3.5, 'sujet')
text(ax, 53, 21, '128,02°', 'limite', 's'); text(ax, 69, 21, '100°', 'sujet', 's')
text(ax, 18, 4.5, 'se ferme : B ≈ 51,98°', 'resultat', 's'); text(ax, 68, 4.5, 'ne se ferme pas : exclu', 'limite', 's')
save(fig, '36-104')
