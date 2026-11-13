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
P=sqdraw(ax,24,32,26,['sujet']*4,list('ABCD'),r=2.4)
def sh(a,b,k):
    dx=b[0]-a[0];dy=b[1]-a[1];L=(dx*dx+dy*dy)**.5
    return (a[0]+dx*k/L,a[1]+dy*k/L),(b[0]-dx*k/L,b[1]-dy*k/L)
for j in (1,2,3):
    p,q=sh(P[0],P[j],3.4); arrow(ax,p,q,'varie')
box(ax,5,16,38,32,'sujet',fill=False,dash=True,lw=1.0)
text(ax,24,56,r'orbite de A = {A, B, C, D}','sujet','m')
text(ax,24,10,'action transitive','varie','m')
Q=sqv(66,32,20)
poly(ax,Q,'fixe',fill=False)
axis(ax,Q,2.4,'autre')
for i,l in enumerate('ABCD'):
    disc(ax,Q[i][0],Q[i][1],2.4,'autre' if i in (0,2) else 'fixe',label=l,size='s')
text(ax,66,52,r'axe de $s$ : A et C fixes','autre','s')
box(ax,48,5,36,10,'autre',label=r'Stab A = {1, $s$}',size='m',weight='bold',lw=1.2)
save(fig,'49-145')
