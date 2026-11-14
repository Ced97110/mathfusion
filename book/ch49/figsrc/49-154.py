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
box(ax,2,12,40,35,'fixe'); box(ax,46,12,40,35,'fixe')
text(ax,22,42,r'$G$ : 8 gestes','fixe','s'); text(ax,66,42,r'$S$ : 4 sommets','fixe','s')
for k in range(8):
    x=8+9*(k%4); y=33-10*(k//4)
    if k==0: disc(ax,x,y,3,'sujet',label='1')
    elif k==1: disc(ax,x,y,3,'sujet',label=r'$s$')
    else: disc(ax,x,y,3,'fixe')
Q=sqv(66,26,14); poly(ax,Q,'fixe',fill=False)
for i,l in enumerate('1234'): disc(ax,Q[i][0],Q[i][1],3,'autre' if i in (0,2) else 'fixe',label=l)
text(ax,22,54,'Stab 1 : des gestes','sujet','m'); text(ax,66,54,'Fix s : des sommets','autre','m')
text(ax,22,6,'2 gestes sur 8','sujet','s'); text(ax,66,6,'2 sommets sur 4','autre','s')
save(fig,'49-154')
