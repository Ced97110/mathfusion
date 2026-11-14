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

fig, ax = canvas(110); k = 0.3
A = (30, 70); c50, s50 = math.cos(math.radians(50)), math.sin(math.radians(50))
B = (A[0]+90*k, A[1]); C = (A[0]+120*k*c50, A[1]+120*k*s50); D = (C[0], A[1]); G = cen(A, B, C)
poly(ax, [A, D, C], 'sujet'); poly(ax, [D, B, C], 'autre')
line(ax, [A, B, C, A], 'encre', 1.2); line(ax, [C, D], 'encre', 1.2, True); rmark(ax, D, (-1, 0), (0, 1), 2.0)
text(ax, D[0]-2.5, 84, r'$h$', 'encre', 'm')
q = out(A, C, G, 4); text(ax, q[0], q[1], r'$b$', 'sujet', 'm'); q = out(B, C, G, 4); text(ax, q[0], q[1], r'$a$', 'autre', 'm')
text(ax, 21, 72, '50°', 'sujet', 's'); text(ax, 69, 72, '82,03°', 'autre', 's')
box(ax, 3, 36, 82, 25, 'fixe'); text(ax, 44, 57, 'départ : deux écritures de h', 'fixe', 's')
text(ax, 44, 50, r'$h=b\,\sin A=120\times0{,}7660$', 'sujet'); text(ax, 44, 42, r'$h=a\,\sin B=92{,}82\times0{,}9903$', 'autre')
arrow(ax, (44, 35), (44, 32), 'varie')
box(ax, 3, 15, 82, 16, 'varie'); text(ax, 44, 27, 'étape clé : même h, on égale', 'varie', 's')
text(ax, 44, 20, r'$b\,\sin A=a\,\sin B\ (\approx91{,}92)$', 'varie')
arrow(ax, (44, 14), (44, 11), 'resultat')
box(ax, 3, 1, 82, 9.5, 'resultat', label=r'$a/\sin A=b/\sin B$')
save(fig, '36-023')
