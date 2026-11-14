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
fig, ax = canvas(66)
text(ax, 44, 60, r'$\sin^{-1}\,0{,}5 = 30°$', 'sujet', 'xl')
box(ax, 6, 34, 20, 11, 'fixe', label='0,5', size='l')
arrow(ax, (26, 39.5), (58, 39.5), 'varie')
text(ax, 42, 43.5, r'$\sin^{-1}$', 'varie', 'm')
box(ax, 58, 34, 24, 11, 'resultat', label='30°', size='l')
text(ax, 16, 30.5, 'nombre', 'fixe', 's'); text(ax, 70, 30.5, 'angle', 'resultat', 's')
box(ax, 4, 9, 38, 11, 'limite', label=r'$1/\sin\,30° = 2$')
line(ax, [(6, 11), (40, 18)], 'limite', lw=1.1)
box(ax, 46, 9, 38, 11, 'sujet', label=r'$\arcsin\,0{,}5 = 30°$')
text(ax, 23, 4.5, 'inverse du sinus : faux', 'limite', 's'); text(ax, 65, 4.5, 'nom français, même angle', 'sujet', 's')
save(fig, '36-097')
