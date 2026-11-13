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

fig, ax = canvas(98); V = (16, 52); L = 42
c50, s50 = math.cos(math.radians(50)), math.sin(math.radians(50))
P = (V[0]+L, V[1]); Q = (V[0]+L*c50, V[1]+L*s50)
line(ax, [V, P], 'fixe', 1.2); line(ax, [V, Q], 'fixe', 1.2)
arc(ax, V, 15, 0, 50, 'sujet', 1.6)
q = (V[0]+25*math.cos(math.radians(25)), V[1]+25*math.sin(math.radians(25))); text(ax, q[0], q[1], '50°', 'sujet')
disc(ax, V[0], V[1], 1.3, 'sujet'); text(ax, V[0]-4, V[1]-3.5, 'A', 'sujet', 'l')
box(ax, 6, 14, 24, 14, 'sujet', label=r'$A$', size='xl'); text(ax, 45, 21, '=', 'encre', 'xl')
box(ax, 60, 14, 22, 14, 'sujet', label='50°', size='xl')
text(ax, 18, 8, "l'angle au coin A", 'sujet', 's'); text(ax, 45, 8, 'mesure', 'encre', 's'); text(ax, 71, 8, '50 degrés', 'sujet', 's')
arrow(ax, (18, 29), (V[0]+14.5, V[1]-2), 'sujet')
arrow(ax, (64, 29), (q[0]+1, q[1]-3), 'sujet')
save(fig, '36-015')
