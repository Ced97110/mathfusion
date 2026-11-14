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

fig,ax=canvas(62)
P=Pm(22,22,8); axes(ax,P,-2.5,3.2,-1.2,3.2)
a=P(2,1); b=P(-1,2); o=P(0,0)
line(ax,[o,a],'sujet',lw=0.7,dash=True); line(ax,[o,b],'resultat',lw=0.7,dash=True)
dot(ax,a,'sujet'); dot(ax,b,'resultat'); dot(ax,o,'fixe',0.8)
text(ax,a[0]+8,a[1]-3,'(2 ; 1)','sujet','s'); text(ax,b[0]-1,b[1]+4,'(−1 ; 2)','resultat','s')
ang=math.degrees(math.atan2(1,2)); arc(ax,o,7,ang+2,ang+88,'varie'); text(ax,o[0]+3.5,o[1]+11,'90°','varie','s')
# matrix
mx,my=64,50
line(ax,[(mx-9,my+7),(mx-11,my+7),(mx-11,my-7),(mx-9,my-7)],'encre'); line(ax,[(mx+9,my+7),(mx+11,my+7),(mx+11,my-7),(mx+9,my-7)],'encre')
for t,dx,dy in (('0',-5,4),('−1',5,4),('1',-5,-4),('0',5,-4)): text(ax,mx+dx,my+dy,t,'sujet','m')
text(ax,mx-17,my,r'$R_{90°}$','sujet','m')
text(ax,64,34,r'$0\times2+(-1)\times1=-1$','varie','s')
text(ax,64,28,r'$1\times2+0\times1=2$','varie','s')
text(ax,64,18,'déterminant : 1','fixe','s')
save(fig,'74-035')
