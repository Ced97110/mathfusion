import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def U(p, q):
    d = math.hypot(q[0]-p[0], q[1]-p[1]); return ((q[0]-p[0])/d, (q[1]-p[1])/d)
def ang(p, q): return math.degrees(math.atan2(q[1]-p[1], q[0]-p[0]))
def arc(ax, c, r, a0, a1, role='encre', lw=0.9, dash=False):
    pts = [(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/40)), c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/40))) for i in range(41)]
    line(ax, pts, role, lw, dash)
def rmark(ax, v, d1, d2, s=2.4, role='encre'):
    line(ax, [(v[0]+d1[0]*s, v[1]+d1[1]*s), (v[0]+(d1[0]+d2[0])*s, v[1]+(d1[1]+d2[1])*s), (v[0]+d2[0]*s, v[1]+d2[1]*s)], role, 0.7)
def M(p, q, t=0.5): return (p[0]+(q[0]-p[0])*t, p[1]+(q[1]-p[1])*t)
def out(p, q, G, k):
    m = M(p, q); d = U(p, q); n = (-d[1], d[0])
    if (m[0]-G[0])*n[0] + (m[1]-G[1])*n[1] < 0: n = (-n[0], -n[1])
    return (m[0]+n[0]*k, m[1]+n[1]*k)
def away(V, G, k):
    d = U(G, V); return (V[0]+d[0]*k, V[1]+d[1]*k)
def cen(*P): return (sum(p[0] for p in P)/len(P), sum(p[1] for p in P)/len(P))
def field(s=0.55, A=(14, 10)):
    c, sn = math.cos(math.radians(50)), math.sin(math.radians(50))
    return A, (A[0]+90*s, A[1]), (A[0]+120*s*c, A[1]+120*s*sn)
def gtri(x0=6.5, y0=10, u=7.5):
    return (x0, y0), (x0+10*u, y0), (x0+3*u, y0+4*u), (x0+3*u, y0)
def bis(V, P, Q, r):
    a = U(V, P); b = U(V, Q); s = (a[0]+b[0], a[1]+b[1]); n = math.hypot(*s)
    return (V[0]+s[0]/n*r, V[1]+s[1]/n*r)
def anglearc(ax, V, P, Q, r, role='encre'):
    a0, a1 = ang(V, P), ang(V, Q)
    while a1-a0 > 180: a1 -= 360
    while a0-a1 > 180: a0 -= 360
    arc(ax, V, r, a0, a1, role)
def pointer(ax, p, q, role='varie'):
    arrow(ax, p, q, role, lw=0.9)

fig, ax = canvas(64); u = 7.0; A, B, C, D = gtri(y0=22, u=u); G = cen(A, B, C)
poly(ax, [A, D, C], 'sujet'); poly(ax, [D, B, C], 'autre')
line(ax, [A, B, C, A], 'encre', 1.3); line(ax, [C, D], 'encre', 1.3, True)
rmark(ax, D, (-1, 0), (0, 1)); rmark(ax, D, (1, 0), (0, 1))
anglearc(ax, A, D, C, 6, 'sujet'); anglearc(ax, B, D, C, 6, 'autre')
text(ax, A[0]-3.5, 19, 'A', 'sujet', 'l'); text(ax, B[0]+3.5, 19, 'B', 'autre', 'l')
text(ax, D[0]+2, 22+2*u, r'$h=4$', 'encre', ha='left')
q = out(A, C, G, 7); text(ax, q[0], q[1], r'$b=5$', 'sujet')
q = out(B, C, G, 8); text(ax, q[0], q[1], r'$a\approx8{,}06$', 'autre')
box(ax, 3, 3, 40, 11, 'sujet', label=r'$\sin A=\frac{4}{5}=0{,}8$', size='s')
box(ax, 45, 3, 40, 11, 'autre', label=r'$\sin B=\frac{4}{8{,}06}\approx0{,}496$', size='s')
save(fig, '36-009')
