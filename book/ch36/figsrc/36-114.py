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
fig, ax = canvas(58)
x0 = 16; sc = 3.0
rows = [(4, -36, '0 triangle', 'limite'), (5, 0, '1 triangle', 'resultat'), (7, 96, '2 triangles', 'resultat'), (12, 476, '1 seul triangle', 'varie')]
line(ax, [(x0 + 5*sc, 6), (x0 + 5*sc, 46)], 'fixe', dash=True); line(ax, [(x0 + 10*sc, 6), (x0 + 10*sc, 46)], 'fixe', dash=True)
text(ax, x0 + 5*sc, 50, 'h = 5', 'fixe', 's'); text(ax, x0 + 10*sc, 50, 'b = 10', 'fixe', 's')
for i, (a_, D, res, role) in enumerate(rows):
    y = 36 - 10*i
    text(ax, 2, y + 3, f'a = {a_}', 'sujet', 's', ha='left')
    box(ax, x0, y, a_*sc, 6, 'sujet', r=0.4)
    text(ax, 56, y + 3, r'$\Delta = %s$ : %s' % (str(D).replace('-', '-'), res) if D >= 0 else r'$\Delta = -36$ : %s' % res, role, 's', ha='left')
save(fig, '36-114')
