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

fig, ax = canvas(58)
k = 4.5; O = (8, 25); ay = O[1]
tip = (O[0]+10*math.cos(math.radians(30))*k, ay+5*k)
dx = math.sqrt(49-25)
X1 = (O[0]+(10*math.cos(math.radians(30))-dx)*k, ay); X2 = (O[0]+(10*math.cos(math.radians(30))+dx)*k, ay)
line(ax, [(4, ay), (80, ay)], 'fixe', 1.0)
poly(ax, [O, X1, tip], 'sujet'); poly(ax, [O, X2, tip], 'autre', fill=False)
line(ax, [O, tip], 'sujet', 1.6)
line(ax, [tip, X1], 'sujet', 1.3); line(ax, [tip, X2], 'autre', 1.3)
line(ax, [tip, (tip[0], ay)], 'fixe', 0.8, True)
arc(ax, tip, 4*k, 240, 300, 'limite', 0.9, True)
text(ax, tip[0]+9, tip[1]+3, '4 cm : aucun', 'limite', 's')
arc(ax, O, 12, 0, 30, 'sujet')
text(ax, 25, ay+3.5, '30°', 'sujet', 's')
q = (O[0]+tip[0])/2-5, (O[1]+tip[1])/2+4; text(ax, q[0], q[1], '10 cm', 'sujet')
text(ax, tip[0]+2, ay+10, '5 cm', 'fixe', 's', ha='left')
text(ax, 42, ay+7, '7 cm', 'sujet', 's'); text(ax, 62, ay+15, '7 cm', 'autre', 's'); text(ax, 77, ay+2.5, 'règle', 'fixe', 's')
arrow(ax, (O[0], ay-5), (X1[0], ay-5), 'sujet', both=True); text(ax, (O[0]+X1[0])/2, ay-8.5, '3,76 cm', 'sujet', 's')
arrow(ax, (O[0], ay-12), (X2[0], ay-12), 'autre', both=True); text(ax, (O[0]+X2[0])/2, ay-15.5, '13,56 cm', 'autre', 's')
save(fig, '36-005')
