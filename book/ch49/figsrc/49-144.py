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
fig,ax=canvas(48)
bw=17;gap=3;x0=(88-4*bw-3*gap)/2
for i in range(4):
    x=x0+i*(bw+gap); role='sujet' if i==0 else 'fixe'
    box(ax,x,24,bw,13,role,dash=(i>0))
    for j in range(2): disc(ax,x+bw/2-3.5+7*j,28.5,2.2,role)
text(ax,x0+bw/2,33.5,'H','sujet','s')
brace(ax,x0,x0+4*bw+3*gap,37,'fixe',label=r'$G$ : 8 éléments',down=False)
brace(ax,x0,x0+4*bw+3*gap,24,'fixe',label='4 classes latérales')
box(ax,28,3,32,10,'resultat',label=r'$[G : H] = 4$',size='l')
save(fig,'49-144')
