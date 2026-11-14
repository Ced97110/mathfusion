import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
a, b, c = 40, 50, 60; s = (a + b + c) / 2
Ax = (c*c + a*a - b*b) / (2*a); A = (Ax, math.sqrt(c*c - Ax*Ax)); B = (0.0, 0.0); C = (float(a), 0.0)
k, ox, oy = 0.72, 14, 45
T = lambda p: (ox + k*p[0], oy + k*p[1])
def along(p, q, d):
    L = math.hypot(q[0]-p[0], q[1]-p[1]); return (p[0] + (q[0]-p[0])*d/L, p[1] + (q[1]-p[1])*d/L)
R = along(A, B, s); Q = along(A, C, s); P = (s - c, 0.0)
ra = math.sqrt(s*(s-a)*(s-b)*(s-c))/(s-a); Ia = (P[0], -ra)
fig, ax = canvas(86)
disc(ax, *T(Ia), ra*k, 'fixe', fill=False)
line(ax, [T(A), T(B)], 'sujet', 1.4); line(ax, [T(A), T(C)], 'sujet', 1.4)
line(ax, [T(B), T(R)], 'varie', 1.4); line(ax, [T(B), T(P)], 'varie', 1.4)
line(ax, [T(C), T(Q)], 'autre', 1.4); line(ax, [T(P), T(C)], 'autre', 1.4)
for p in (P, Q, R): disc(ax, *T(p), 0.8, 'encre')
sh = lambda p, dx, dy: (T(p)[0] + dx, T(p)[1] + dy)
for nm, p, d in (('A', A, (0, 3.2)), ('B', B, (-3, 2.2)), ('C', C, (3, 2.2)), ('P', P, (0, 3)), ('Q', Q, (3.2, 0)), ('R', R, (-3.2, 0))):
    text(ax, *sh(p, *d), nm, 'encre', 'l', weight='bold')
mid = lambda p, q: ((p[0]+q[0])/2, (p[1]+q[1])/2)
text(ax, *sh(mid(A, B), -3.5, 0), '60', 'sujet', 'm')
text(ax, *sh(mid(A, C), 3.5, 0), '50', 'sujet', 'm')
text(ax, *sh(mid(B, R), -2.8, 0), '15', 'varie', 'm', weight='bold')
text(ax, *sh(mid(C, Q), 3.0, 0), '25', 'autre', 'm', weight='bold')
text(ax, 69, 76, 'AR + AQ = 60 + 50 + BR + CQ', 'sujet', 's')
text(ax, 69, 66, 'BR devient BP, CQ devient CP', 'varie', 's', weight='bold')
text(ax, 69, 56, 'AR + AQ = 60 + 50 + 40 = 150', 'sujet', 's')
text(ax, 69, 46, 'AR = AQ = 75', 'resultat', 'm', weight='bold')
save(fig, '37-073')
