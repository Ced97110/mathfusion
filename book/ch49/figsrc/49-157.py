import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def sqv(cx,cy,s):
    h=s/2; return [(cx-h,cy-h),(cx+h,cy-h),(cx+h,cy+h),(cx-h,cy+h)]
def sqdraw(ax,cx,cy,s,roles,labels=None,r=2.0,size='s'):
    P=sqv(cx,cy,s); poly(ax,P,'fixe',fill=False)
    for i,p in enumerate(P):
        disc(ax,p[0],p[1],r,roles[i],label=None if labels is None else labels[i],size=size)
    return P
def edge_arrows(ax,P,r,role='varie'):
    for i in range(4):
        a=P[i]; b=P[(i+1)%4]; dx=b[0]-a[0]; dy=b[1]-a[1]; L=(dx*dx+dy*dy)**.5; k=(r+0.8)/L
        arrow(ax,(a[0]+dx*k,a[1]+dy*k),(b[0]-dx*k,b[1]-dy*k),role)
def axis(ax,P,r,role='varie'):
    d=0.7071; a=P[0]; c=P[2]; k=r+0.4
    seg=lambda p,q,m,n: line(ax,[(p[0]+d*m,p[1]+d*m),(q[0]+d*n,q[1]+d*n)],role,dash=True)
    seg(a,a,-4.8,-k); seg(a,c,k,-k); seg(c,c,k,4.8)
fig,ax=canvas(76)
ys=[60,46,32,18]; L=list('ABCD'); H=[r'$H$',r'$rH$',r'$r^2H$',r'$r^3H$']
text(ax,14,70,'sommets','fixe','m'); text(ax,60,70,'classes de Stab A','fixe','m')
for y,l,h in zip(ys,L,H):
    disc(ax,14,y,3.5,'sujet',label=l)
    box(ax,42,y-5.5,38,11,'autre')
    text(ax,50,y,h,'autre','s')
    disc(ax,64,y,2,'autre'); disc(ax,73,y,2,'autre')
    arrow(ax,(18,y),(41.2,y),'resultat',both=True)
arrow(ax,(6,ys[0]-1.5),(6,ys[1]+1.5),'varie'); text(ax,2.5,(ys[0]+ys[1])/2,r'$r$','varie','s')
arrow(ax,(83.5,ys[0]-1.5),(83.5,ys[1]+1.5),'varie'); text(ax,86.3,(ys[0]+ys[1])/2,r'$r$','varie','s')
save(fig,'49-157')
