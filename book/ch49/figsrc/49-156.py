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
fig,ax=canvas(80)
top=64; rh=5.6; x0=34; cw=12
yc=lambda i: top-rh*(i+0.5)
box(ax,x0,top-8*rh,4*cw,8*rh,'fixe',fill=False,lw=0.6)
for i in range(1,8): line(ax,[(x0,top-i*rh),(x0+4*cw,top-i*rh)],'fixe',lw=0.4)
for j in range(1,4): line(ax,[(x0+j*cw,top),(x0+j*cw,top-8*rh)],'fixe',lw=0.4)
for j,l in enumerate('ABCD'): text(ax,x0+cw*(j+.5),top+5.5,l,'encre','m')
box(ax,x0,top-8*rh,cw,8*rh,'sujet',fill=False,lw=1.4)
box(ax,x0-1,top-2*rh,4*cw+2,rh,'varie',fill=False,lw=1.4)
X={0:[0,1,2,3],1:[0,2],2:[1,3]}
for i,cols in X.items():
    for j in cols: disc(ax,x0+cw*(j+.5),yc(i),1.7,'resultat')
for i,t in enumerate(['1',r'$s$',r"$s'$"]): text(ax,x0-3,yc(i),t,'encre','s',ha='right')
text(ax,x0-3,(yc(3)+yc(7))/2,'5 autres :\naucune','fixe','s',ha='right')
text(ax,36,13,'ligne : Fix g','varie','s',ha='left')
text(ax,36,8,'colonne : Stab x','sujet','s',ha='left')
text(ax,70,10.5,'8 croix','resultat','m')
save(fig,'49-156')
