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
text(ax, 44, 57, r'$\Delta \approx 576{,}9$   $\sqrt{\Delta} \approx 24{,}02$', 'sujet', 'm')
text(ax, 44, 62.5, 'nombres de l’équation : 30,64 et 90,48', 'fixe', 's')
f = numberline(ax, 8, 78, 20, 0, 30, 5, arrow_right=False, every=2)
text(ax, 83, 20, r'$c$', 'encre', 'm')
for v, role, lab in ((3.31, 'resultat', '3,31'), (27.33, 'resultat', '27,33'), (15.32, 'fixe', '15,32')):
    disc(ax, f(v), 20, 1.3, role); text(ax, f(v), 25, lab, role, 's')
    line(ax, [(f(v), 27), (f(v), 38)], role, dash=True)
arrow(ax, (f(15.32), 36), (f(27.33), 36), 'varie'); arrow(ax, (f(15.32), 36), (f(3.31), 36), 'varie')
text(ax, (f(15.32) + f(27.33))/2, 40, '+ 12,01', 'varie', 's'); text(ax, (f(15.32) + f(3.31))/2, 40, '− 12,01', 'varie', 's')
text(ax, 44, 47, '30,64 ÷ 2 = 15,32', 'fixe', 's')
text(ax, 44, 6, 'deux longueurs c possibles : 3,31 et 27,33', 'resultat', 's')
save(fig, '36-111')
