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
fig,ax=canvas(72)
text(ax,44,66,r'$g$ parcourt les 8 éléments','encre','m')
box(ax,4,42,38,12,'resultat'); box(ax,46,42,38,12,'limite')
for i in range(4):
    disc(ax,4+4.75+9.5*i,48,2.6,'resultat'); disc(ax,46+4.75+9.5*i,48,2.6,'limite')
text(ax,23,59,'commutent avec r : 4','resultat','s')
text(ax,65,59,'pas : 4 réflexions','limite','s')
arrow(ax,(36,41),(36,26.5),'fixe'); arrow(ax,(52,41),(52,26.5),'varie')
text(ax,33,34,r'$g\,r\,g^{-1} = r$','fixe','s',ha='right')
text(ax,54.5,34,r'$g\,r\,g^{-1} = r^3$','varie','s',ha='left')
box(ax,26,8,36,17,'resultat',dash=True)
disc(ax,36,16.5,3.8,'sujet',label=r'$r$'); disc(ax,52,16.5,3.8,'sujet',label=r'$r^3$')
text(ax,44,3.5,'classe de r : 2, pas 1','encre','s')
save(fig,'49-149')
