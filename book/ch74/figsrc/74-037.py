import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def Pm(ox, oy, s): return lambda x, y: (ox + x * s, oy + y * s)
def axes(ax, P, x0, x1, y0, y1):
    line(ax, [P(x0, 0), P(x1, 0)], 'fixe', lw=0.5); line(ax, [P(0, y0), P(0, y1)], 'fixe', lw=0.5)
def dot(ax, p, role, r=1.1): disc(ax, p[0], p[1], r, role)
def arc(ax, c, r, a0, a1, role, lw=1.0):
    n = 24; pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-3], pts[-1], role, lw=lw)
def tf(pts, o, ang=0, mir=False):
    a = math.radians(ang); out = []
    for x, y in pts:
        if mir: x = -x
        out.append((o[0] + x * math.cos(a) - y * math.sin(a), o[1] + x * math.sin(a) + y * math.cos(a)))
    return out

fig,ax=canvas(72)
c=(44,36); R=20; P=Pm(c[0],c[1],R)
arc_pts=[(c[0]+R*math.cos(math.radians(t)),c[1]+R*math.sin(math.radians(t))) for t in range(0,361,6)]
line(ax,arc_pts,'fixe',lw=0.8)
axes(ax,P,-1.25,1.25,-1.25,1.25)
line(ax,[P(-0.8,0.6),P(0.8,-0.6)],'fixe',lw=0.5,dash=True)
u=P(0.6,0.8); v1=P(-0.8,0.6); v2=P(0.8,-0.6)
arrow(ax,c,u,'sujet',lw=1.2); arrow(ax,c,v1,'resultat',lw=1.0); arrow(ax,c,v2,'limite' if False else 'resultat',lw=1.0)
for p,r in ((u,'sujet'),(v1,'resultat'),(v2,'resultat')): dot(ax,p,r,1.3)
q=3.2; line(ax,[(c[0]+q*0.6,c[1]+q*0.8),(c[0]+q*0.6-q*0.8,c[1]+q*0.8+q*0.6),(c[0]-q*0.8,c[1]+q*0.6)],'fixe',lw=0.6)
text(ax,u[0]+2,u[1]+4,'(0,6 ; 0,8)','sujet','s',ha='left'); text(ax,v1[0]-2,v1[1]+4,'(−0,8 ; 0,6)','resultat','s',ha='right')
text(ax,v2[0]+1,v2[1]-4,'(0,8 ; −0,6)','resultat','s',ha='left')
text(ax,u[0]+2,u[1]-0.5,'colonne 1','sujet','s',ha='left')
text(ax,v1[0]-2,v1[1]-0.5,'rotation','resultat','s',ha='right'); text(ax,v2[0]+1,v2[1]-8,'réflexion','resultat','s',ha='left')
text(ax,c[0],6,'cercle de rayon 1 : 2 choix seulement','fixe','s')
save(fig,'74-037')
