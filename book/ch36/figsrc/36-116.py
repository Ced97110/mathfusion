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
x0, x1 = 10, 72
for (y, title, qtxt, roots, cap, capr) in ((48, r'$a = 12 > b = 10$', r'$q = 100 - 144 = -44$', ((-2.25, 'limite', '−2,25'), (19.57, 'resultat', '19,57')), 'une racine négative : refusée', 'limite'),
                                         (18, r'$a = 7 < b = 10$', r'$q = 100 - 49 = 51$', ((3.76, 'resultat', '3,76'), (13.56, 'resultat', '13,56')), 'deux racines positives', 'resultat')):
    f = numberline(ax, x0, x1, y, -5, 20, 5, labels=False, arrow_right=False)
    text(ax, f(0), y - 3.4, '0', 'fixe', 's')
    for v, role, lab in roots:
        disc(ax, f(v), y, 1.4, role); text(ax, f(v), y + 5, lab, role, 's')
    text(ax, 4, y + 12, title + '  ' + qtxt, 'sujet', 's', ha='left')
    text(ax, 44, y - 8, cap, capr, 's')
save(fig, '36-116')
