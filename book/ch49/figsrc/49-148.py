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
fig,ax=canvas(62)
text(ax,43.5,53,'C','sujet',18,ha='right')
text(ax,43.5,53,'(x)','varie',18,ha='left')
arrow(ax,(40,46),(27,39),'fixe'); arrow(ax,(50,46),(62,39),'varie')
text(ax,22,35,'C : le centre du groupe','fixe','s')
text(ax,66,35,r'$x$ : un élément choisi','varie','s')
for i,(l,r_) in enumerate([(r'$C$ : 2 éléments','fixe'),(r'$C(r)$ : 4 éléments','sujet'),(r'$C(s)$ : 4 éléments','sujet')]):
    box(ax,3+i*29,6,26,11,r_,label=l,size='s')
save(fig,'49-148')
