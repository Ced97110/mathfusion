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

fig,ax=canvas(66)
P=Pm(46,10,8.5); axes(ax,P,-4.6,3,-0.5,4.8)
pts={'x':(1,0),'Bx':(0,1),'g':(2,4),'Ag':(-4,2),'f':(-3,2)}
col={'x':'sujet','Bx':'fixe','g':'varie','Ag':'fixe','f':'resultat'}
arc(ax,P(0,0),5.5,3,85,'varie',lw=0.9); text(ax,P(0,0)[0]+9,P(0,0)[1]+8,r'$B$','varie','m')
arrow(ax,P(*pts['Bx']),P(*pts['g']),'varie',lw=1.0); text(ax,P(1,2.5)[0]+5,P(1,2.5)[1]-1,r'$+c$','varie','m')
arrow(ax,P(*pts['g']),P(*pts['Ag']),'varie',lw=1.0); text(ax,P(-1,3.15)[0],P(-1,3.15)[1]+4,r'$A$','varie','m')
arrow(ax,P(*pts['Ag']),P(*pts['f']),'varie',lw=1.0); text(ax,P(-3.5,2)[0],P(-3.5,2)[1]-4,r'$+b$','varie','m')
for k,v in pts.items(): dot(ax,P(*v),col[k],1.3)
text(ax,P(1,0)[0]+2,P(1,0)[1]-4,'(1 ; 0)','sujet','s',ha='left'); text(ax,P(0,1)[0]-2,P(0,1)[1]-3.5,'(0 ; 1)','fixe','s',ha='right')
text(ax,P(2,4)[0]+2,P(2,4)[1]+3,'(2 ; 4)','varie','s',ha='left'); text(ax,P(-4,2)[0]+1,P(-4,2)[1]+4,'(−4 ; 2)','fixe','s',ha='left')
text(ax,P(-3,2)[0]+2,P(-3,2)[1]-8.5,'(−3 ; 2)','resultat','s',ha='left')
text(ax,44,60,r'$f(g(x))=ABx+Ac+b$','encre','m')
save(fig,'74-044')
