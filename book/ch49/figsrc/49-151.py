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
fig,ax=canvas(66)
P=sqdraw(ax,18,36,18,['resultat','fixe','resultat','fixe'],list('1234'),r=2.4)
axis(ax,P,2.4)
text(ax,18,20,r'axe de $g$ par 1 et 3','varie','s')
text(ax,62,60,r'on teste $g\,x = x$','encre','m')
rows=[('1 → 1 : gardé','resultat'),('2 → 4 : écarté','limite'),('3 → 3 : gardé','resultat'),('4 → 2 : écarté','limite')]
for i,(t,r_) in enumerate(rows): box(ax,40,44-i*10,44,8,r_,label=t,size='s')
arrow(ax,(62,13),(62,10.5),'resultat')
box(ax,34,2,50,8,'resultat',label=r'Fix $g$ = {1, 3}')
save(fig,'49-151')
