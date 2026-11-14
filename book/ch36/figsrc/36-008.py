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

fig, ax = canvas(60); u = 7.5; A, B, C, D = gtri(y0=12); x0, y0 = A
Mi = (x0+5*u, y0)
poly(ax, [A, B, C], 'fixe')
line(ax, [A, B], 'fixe', 1.0)
line(ax, [C, A], 'fixe', 1.4); line(ax, [C, B], 'fixe', 1.4); line(ax, [C, Mi], 'fixe', 1.4, True)
line(ax, [C, D], 'sujet', 2.2); rmark(ax, D, (-1, 0), (0, 1), 2.6, 'sujet')
for P in (A, B, Mi, D): disc(ax, P[0], P[1], 0.9, 'fixe' if P != D else 'sujet')
text(ax, C[0], C[1]+4, 'C', 'encre', 'l')
text(ax, 11, y0+14, '5', 'fixe'); text(ax, 57, y0+11, '8,06', 'fixe')
text(ax, 44, y0+18, '4,47', 'fixe', 's')
text(ax, C[0]-3.2, y0+2*u, '4', 'sujet', 'l', weight='bold')
text(ax, A[0], y0-3.8, 'A', 'encre', 'l')
text(ax, Mi[0], y0-3.5, 'milieu', 'fixe', 's'); text(ax, B[0], y0-3.5, 'B', 'encre', 'l')
text(ax, 17, y0+37, 'hauteur : angle droit', 'sujet', 'm'); 
save(fig, '36-008')
