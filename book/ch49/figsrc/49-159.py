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
text(ax,22.5,56,'orbite','sujet','m'); text(ax,61,56,'stabilisateur','autre','m')
def mini(cx,cy,k):
    P=sqv(cx,cy,6)
    poly(ax,P,'fixe',fill=False,lw=0.5)
    for i,p in enumerate(P): disc(ax,p[0],p[1],1.4,'varie' if i==k else 'sujet',lw=0.6)
mini(22.5,42,None)
for i in range(4): mini(7+10.5*i,19,i)
for y,n in ((42,4),(19,1)):
    xs=[52,58,64,70] if n==4 else [61]
    for x in xs: disc(ax,x,y,2,'autre')
    text(ax,46,y,r'$\times$','encre','m'); text(ax,82,y,'= 4','resultat','l')
text(ax,22.5,34,'1 coloration','sujet','s'); text(ax,61,34,'4 rotations','autre','s')
text(ax,22.5,8,'4 colorations','sujet','s'); text(ax,61,8,'1 : le neutre','autre','s')
save(fig,'49-159')
