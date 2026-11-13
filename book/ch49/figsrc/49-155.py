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
fig,ax=canvas(52)
cs=[15,44,73]
sqdraw(ax,cs[0],28,18,['resultat']*4,None,r=2.4)
P=sqdraw(ax,cs[1],28,18,['resultat','fixe','resultat','fixe'],list('ABCD'),r=2.4)
axis(ax,P,2.4)
Q=sqdraw(ax,cs[2],28,18,['fixe']*4,list('ABCD'),r=2.4)
edge_arrows(ax,Q,2.4,'varie')
for x,t in zip(cs,['neutre 1',r'réflexion $s$',r'quart de tour $r$']): text(ax,x,46,t,'varie','s')
for x,t,r_ in zip(cs,['4 points fixes','2 points fixes','0 point fixe'],['resultat','resultat','limite']): text(ax,x,9,t,r_,'s')
save(fig,'49-155')
