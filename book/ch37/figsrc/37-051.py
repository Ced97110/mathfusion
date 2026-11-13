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

fig,ax=canvas(58)
u=3.8; cy=33.0
cx=21.0
disc(ax,cx,cy,5*u,'sujet')
line(ax,[(2,cy-5*u),(40,cy-5*u)],'fixe',1.1)
T=(cx,cy-5*u)
line(ax,[(cx,cy),T],'resultat',1.3); dot(ax,(cx,cy),'sujet'); dot(ax,T,'resultat')
rt(ax,T,(cx,cy),(cx+5,T[1]),2.4)
text(ax,cx+2.2,cy-9.5,'5','resultat','s')
text(ax,cx,56,'touche : 1 point','sujet','s')
text(ax,cx,8,r'rayon $\perp$ à la droite','resultat','s')
cx2=66.0; yl=cy-3*u
disc(ax,cx2,cy,5*u,'sujet')
line(ax,[(46,yl),(87,yl)],'fixe',1.1)
F=(cx2,yl);X=(cx2+4*u,yl)
line(ax,[(cx2,cy),F],'fixe',dash=True); line(ax,[(cx2,cy),X],'limite',1.3); line(ax,[F,X],'fixe',1.1)
for p,r in (((cx2,cy),'sujet'),(F,'fixe'),(X,'limite'),((cx2-4*u,yl),'limite')): dot(ax,p,r)
rt(ax,F,(cx2,cy),X,2.0)
text(ax,cx2-2,cy-5.7,'3','fixe','s')
text(ax,cx2+2*u,yl-2.6,'4','fixe','s')
text(ax,cx2+2*u+3.0,cy-3.0,'5','limite','s')
text(ax,cx2,56,'coupe : 2 points','limite','s')
text(ax,cx2,8,r'rayon pas $\perp$ à la droite','limite','s')
save(fig,'37-051')
