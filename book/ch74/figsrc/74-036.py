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

fig,ax=canvas(76)
def panel(cx,phi,pt,img,mat):
    P=Pm(cx,38,4.6); axes(ax,P,-4.2,4.2,-4.2,4.2)
    h=math.radians(phi/2); L=4.6*4.6
    line(ax,[(cx-L*math.cos(h),38-L*math.sin(h)),(cx+L*math.cos(h),38+L*math.sin(h))],'varie',lw=1.1)
    a=P(*pt); b=P(*img); line(ax,[a,b],'fixe',lw=0.6,dash=True)
    dot(ax,a,'sujet'); dot(ax,b,'resultat')
    text(ax,cx,70,r'réflexion, $\varphi=%d°$'%phi,'encre','s'); text(ax,cx,11,mat,'sujet','s'); text(ax,cx,5,'déterminant : −1','fixe','s')
    return a,b
a,b=panel(22,90,(3,1),(1,3),r'$S=(0\ 1;\ 1\ 0)$')
text(ax,a[0]+1,a[1]-3.5,'(3 ; 1)','sujet','s'); text(ax,b[0]-2,b[1]+3.5,'(1 ; 3)','resultat','s',ha='right')
text(ax,40,56,'axe 45°','varie','s',ha='left')
a,b=panel(66,180,(3,1),(-3,1),r'$S=(-1\ 0;\ 0\ 1)$')
text(ax,a[0]+3,a[1]-3.5,'(3 ; 1)','sujet','s'); text(ax,b[0]-1,b[1]+3.5,'(−3 ; 1)','resultat','s')
text(ax,66,64,'axe vertical','varie','s')
save(fig,'74-036')
