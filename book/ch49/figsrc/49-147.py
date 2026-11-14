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
fig,ax=canvas(78)
xs=[14,30,46,62]; labs=['1',r'$r^2$',r'$r$',r'$r^3$']
box(ax,3,12,82,56,'fixe',fill=False,dash=True)
text(ax,44,73,r'$C(r^2) = G$ : 8 éléments','encre','m')
box(ax,7,41,62,21,'sujet',fill=False,lw=1.3)
box(ax,9,42.5,28,18,'resultat')
for x,l in zip(xs,labs): disc(ax,x,55,3.6,'sujet',label=l)
text(ax,23,45,'centre : 1, r²','resultat','s')
text(ax,54,45,r'$C(r)$ : 4 rotations','sujet','s')
for x in xs: disc(ax,x,26,3.6,'fixe')
text(ax,38,17,'4 réflexions','fixe','s')
save(fig,'49-147')
