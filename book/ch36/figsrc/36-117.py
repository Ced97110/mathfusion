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
fig, ax = canvas(56)
k = 0.8; h = 10.7259*k; yb = 30
for cx, a_, role, c1, c2 in ((15, 16.1, 'resultat', 'a = 16,1', 'Δ > 0 : 2 racines'), (44, 10.7259, 'sujet', 'a = h ≈ 10,73', 'Δ = 0 : 1 racine'), (73, 10.0, 'limite', 'a = 10', 'Δ < 0 : 0 racine')):
    arrow(ax, (cx - 13, yb), (cx + 14, yb), 'fixe')
    line(ax, [(cx, yb), (cx, yb + h)], 'fixe', dash=True); disc(ax, cx, yb + h, a_*k, role, fill=False, lw=1.0); disc(ax, cx, yb + h, 0.9, 'fixe')
    if a_*k > h + 0.05:
        dx = math.sqrt((a_*k)**2 - h**2)
        for sg in (-1, 1): disc(ax, cx + sg*dx, yb, 1.1, role)
    elif abs(a_*k - h) < 0.05: disc(ax, cx, yb, 1.1, role)
    text(ax, cx, yb - 9, c1, role, 's'); text(ax, cx, yb - 14, c2, role, 's')
text(ax, 13, yb + h/2 + 1, 'h', 'fixe', 's', ha='right')
text(ax, 44, 6, 'points du cercle = racines', 'resultat', 's')
save(fig, '36-117')
