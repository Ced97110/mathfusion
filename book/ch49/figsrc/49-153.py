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
text(ax,44,54,r'$|\mathrm{Fix}\,g|$','sujet',18)
text(ax,44,45,'les barres comptent','encre','m')
text(ax,2,30,r'Fix $s$','varie','m',ha='left')
box(ax,18,24,28,12,'resultat')
disc(ax,26,30,3,'resultat',label='1'); disc(ax,38,30,3,'resultat',label='3')
arrow(ax,(49,30),(63,30),'fixe'); text(ax,56,34,'compter','fixe','s')
text(ax,76,30,'2','resultat',18)
text(ax,2,11,r'Fix $r$','varie','m',ha='left')
box(ax,18,5,28,12,'limite',dash=True,label='ensemble vide',size='s')
arrow(ax,(49,11),(63,11),'fixe'); text(ax,56,15,'compter','fixe','s')
text(ax,76,11,'0','resultat',18)
save(fig,'49-153')
