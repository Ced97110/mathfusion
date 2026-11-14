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
fig, ax = canvas(98)
k = 10.5
Pp = (8, 62); Q = (8 + 5*k, 62); R = PT(Pp, 4.40*k, 40)
poly(ax, [Pp, Q, R], 'sujet'); cen = ((Pp[0]+Q[0]+R[0])/3, (Pp[1]+Q[1]+R[1])/3)
angtxt(ax, Pp, Q, R, '40°', 'sujet', d=9); angtxt(ax, Q, Pp, R, '60°', 'resultat', d=8); angtxt(ax, R, Pp, Q, '80°', 'sujet', d=7)
sidetxt(ax, Pp, Q, cen, '5 cm', 'sujet'); sidetxt(ax, Pp, R, cen, '4,40 cm', 'resultat', d=4.5); sidetxt(ax, Q, R, cen, '3,26 cm', 'resultat', d=4.5)
steps = [(r'$180° - 40° - 80° = 60°$', 'varie'), (r'$5 \div \sin 80° \approx 5{,}077$', 'varie'),
         (r'$5{,}077 \times \sin 40° \approx 3{,}26$', 'resultat'), (r'$5{,}077 \times \sin 60° \approx 4{,}40$', 'resultat')]
for i, (s, r_) in enumerate(steps):
    y = 47 - 12*i
    box(ax, 8, y, 72, 9, r_, label=s)
    if i: arrow(ax, (44, y + 12), (44, y + 9), 'fixe')
save(fig, '36-098')
