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
fig,ax=canvas(56)
P=sqdraw(ax,24,28,22,['resultat','fixe','resultat','fixe'],list('1234'),r=2.6,size='m')
axis(ax,P,2.6)
arrow(ax,(P[1][0]-1.8,P[1][1]+1.8),(P[3][0]+1.8,P[3][1]-1.8),'varie',both=True)
text(ax,24,50,r'geste $s$ (réflexion)','varie','m')
text(ax,24,8,r'Fix $s$ = {1, 3}','resultat','m')
Q=sqdraw(ax,64,28,22,['fixe']*4,list('1234'),r=2.6,size='m')
edge_arrows(ax,Q,2.6,'varie')
text(ax,64,50,r'geste $r$ (quart de tour)','varie','m')
text(ax,64,8,'Fix r = ∅','limite','m')
save(fig,'49-150')
