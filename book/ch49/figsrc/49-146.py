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
fig,ax=canvas(60)
disc(ax,12,30,4,'sujet',label=r'$r$',size='m')
text(ax,12,21,'quart de tour','sujet','s')
box(ax,58,10,26,38,'resultat',dash=True)
disc(ax,71,38,4,'sujet',label=r'$r$')
disc(ax,71,20,4,'sujet',label=r'$r^3$')
arrow(ax,(17,31.5),(66,37.5),'fixe')
arrow(ax,(17,28.5),(66,21.5),'varie')
text(ax,40,38.5,'rotation : r','fixe','s')
text(ax,40,21.5,r'réflexion : $r^3$','varie','s')
text(ax,44,55,r'$g\,r\,g^{-1}$ pour chaque $g$','encre','m')
text(ax,71,5,'classe de r','resultat','s')
save(fig,'49-146')
