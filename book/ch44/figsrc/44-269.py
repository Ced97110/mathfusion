import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def ring(cx,cy,R,labs,role,r,col,size):
    P=[(cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))) for a in (90,-30,210)]
    for i in range(3):
        p,q=P[i],P[(i+1)%3]; d=math.hypot(q[0]-p[0],q[1]-p[1]); u=((q[0]-p[0])/d,(q[1]-p[1])/d)
        k=r+1.2; arrow(ax,(p[0]+u[0]*k,p[1]+u[1]*k),(q[0]-u[0]*k,q[1]-u[1]*k),col,curve=-0.25)
    for p,s in zip(P,labs): disc(ax,p[0],p[1],r,role,label=s,size=size)
text(ax,22,58,r'puissances de $\sigma$','sujet','m'); text(ax,66,58,r'cycle de $\sigma$','autre','m')
ring(22,32,14,[r'$\sigma$',r'$\sigma^{2}$',r'$\sigma^{3}=1$'],'sujet',6.5,'varie','s')
ring(66,32,13,['1','2','3'],'autre',5,'varie','m')
text(ax,22,7,'groupe cyclique','sujet','s'); text(ax,66,7,r'$1\to2\to3\to1$','autre','s')
save(fig,'44-269')
