import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def dist(p, q): return math.hypot(q[0] - p[0], q[1] - p[1])
def U(p, q):
    d = dist(p, q); return ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
def mix(p, q, t): return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
def off(p, d, q):
    u = U(q, p); return (p[0] + u[0] * d, p[1] + u[1] * d)
def onseg(p, q, t, d=0.0):
    u = U(p, q); n = (-u[1], u[0]); m = mix(p, q, t); return (m[0] + n[0] * d, m[1] + n[1] * d)
def dot(ax, p, role='encre', r=0.6): ax.add_patch(Circle(p, r, fc=COL[role], ec=COL[role], zorder=4))
def arc(ax, c, r, t1, t2, role='varie', lw=0.9): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def arcb(ax, v, p, q, r, role='varie', lw=0.9):
    a1 = math.degrees(math.atan2(p[1] - v[1], p[0] - v[0])) % 360; a2 = math.degrees(math.atan2(q[1] - v[1], q[0] - v[0])) % 360
    if (a2 - a1) % 360 > 180: a1, a2 = a2, a1
    if a2 < a1: a2 += 360
    arc(ax, v, r, a1, a2, role, lw)
def foot(p, q, x):
    u = U(p, q); t = (x[0] - p[0]) * u[0] + (x[1] - p[1]) * u[1]; return (p[0] + u[0] * t, p[1] + u[1] * t)
def rt(ax, v, p, q, s=2.0, role='encre'):
    u = U(v, p); w = U(v, q)
    a = (v[0] + u[0] * s, v[1] + u[1] * s); b = (a[0] + w[0] * s, a[1] + w[1] * s); c = (v[0] + w[0] * s, v[1] + w[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
def circum(a, b, c):
    d = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    ux = ((a[0]**2 + a[1]**2) * (b[1] - c[1]) + (b[0]**2 + b[1]**2) * (c[1] - a[1]) + (c[0]**2 + c[1]**2) * (a[1] - b[1])) / d
    uy = ((a[0]**2 + a[1]**2) * (c[0] - b[0]) + (b[0]**2 + b[1]**2) * (a[0] - c[0]) + (c[0]**2 + c[1]**2) * (b[0] - a[0])) / d
    return (ux, uy)
def champ(S, ox, oy):
    a, b, c, s = 40.0, 50.0, 60.0, 75.0
    Cx = 37.5; Cy = math.sqrt(b * b - Cx * Cx); D = math.sqrt(s * (s - a) * (s - b) * (s - c)); r = D / s
    f = lambda p: (ox + S * p[0], oy + S * p[1])
    A = f((0, 0)); B = f((c, 0)); C = f((Cx, Cy)); I = f((s - a, r)); Ia = f((75.0, D / (s - a)))
    Ib = f(((-b * c + c * Cx) / (a - b + c), c * Cy / (a - b + c))); Ic = f(((b * c - c * Cx) / (a + b - c), -c * Cy / (a + b - c)))
    return dict(A=A, B=B, C=C, I=I, Ia=Ia, Ib=Ib, Ic=Ic, r=S * r, ra=S * D / (s - a), rb=S * D / (s - b), rc=S * D / (s - c),
                N=foot(A, B, I), M=foot(A, C, I), L=foot(B, C, I), P=foot(B, C, Ia), Q=foot(A, C, Ia), R=foot(A, B, Ia), f=f)

fig,ax=canvas(110)
S=0.5; g=champ(S,29.5,68.0)
A,Bp,C,I=g['A'],g['B'],g['C'],g['I']
A0,B0,C0=(0,0),(60,0),(37.5,math.sqrt(2500-37.5**2))
def clip(P0,Q0):
    L=dist(P0,Q0); ux=(Q0[0]-P0[0])/L; uy=(Q0[1]-P0[1])/L; pts=[]
    for i in range(-600,601):
        t=i*0.5; p=(P0[0]+ux*t,P0[1]+uy*t)
        if -55<=p[0]<=103 and -132<=p[1]<=80: pts.append(g['f'](p))
    return pts
for P0,Q0 in ((A0,B0),(B0,C0),(C0,A0)):
    pts=clip(P0,Q0); line(ax,[pts[0],pts[-1]],'fixe',0.7,dash=True)
poly(ax,[A,Bp,C],'fixe')
for key,rk,role in (('Ia','ra','autre'),('Ib','rb','autre'),('Ic','rc','autre')):
    c=g[key]; disc(ax,c[0],c[1],g[rk],role,lw=0.9)
disc(ax,I[0],I[1],g['r'],'sujet',lw=0.9)
for key,rk,nm,val in (('Ia','ra',r'$I_a$','28,35'),('Ib','rb',r'$I_b$','39,69'),('Ic','rc',r'$I_c$','66,14')):
    c=g[key]; text(ax,c[0],c[1]+2.4,nm,'autre'); text(ax,c[0],c[1]-2.2,val,'autre','s')
text(ax,I[0],I[1]+2.6,'I','sujet'); text(ax,I[0],I[1]-2.4,'13,23','sujet','s')
text(ax,A[0]-2.6,A[1]-2.4,'A'); text(ax,Bp[0]+2.6,Bp[1]-2.6,'B'); text(ax,C[0]-0.5,C[1]+3.0,'C')
save(fig,'37-068')
