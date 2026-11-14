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
k = 7.2
Pp = (5, 12); Q = (5 + 5*k, 12); R = PT(Pp, 4.40*k, 40)
poly(ax, [Pp, Q, R], 'sujet'); cen = ((Pp[0]+Q[0]+R[0])/3, (Pp[1]+Q[1]+R[1])/3)
angtxt(ax, Pp, Q, R, '40°', 'sujet', d=8); angtxt(ax, Q, Pp, R, '60°', 'sujet', d=6.5); angtxt(ax, R, Pp, Q, '80°', 'sujet', d=6)
sidetxt(ax, Pp, Q, cen, '5', 'resultat'); sidetxt(ax, Pp, R, cen, '4,40', 'resultat'); sidetxt(ax, Q, R, cen, '3,26', 'resultat')
for x, v, a in ((50, 3.26, '40°'), (62, 4.40, '60°'), (74, 5, '80°')):
    box(ax, x, 12, 9, v*7, 'resultat'); text(ax, x + 4.5, 12 + v*7 + 3, {3.26:'3,26',4.40:'4,40',5:'5'}[v], 'resultat', 's')
    text(ax, x + 4.5, 8, a, 'sujet', 's')
text(ax, 62, 56, 'petit angle, petit côté', 'fixe', 's')
save(fig, '36-099')
