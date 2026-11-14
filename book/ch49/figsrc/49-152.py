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
text(ax,43,56,'Fix','sujet',20,ha='right'); text(ax,44,56,r'$g$','varie',20,ha='left')
text(ax,44,47,r'points que $g$ laisse en place','encre','m')
xs=[36,45,54,63]
for x,l in zip(xs,'1234'): text(ax,x,39.5,l,'fixe','s')
data=[('neutre',[1,1,1,1],'4 points'),(r'réflexion $s$',[1,0,1,0],'2 points'),(r'quart de tour $r$',[0,0,0,0],'0 point')]
for k,(lab,m,cnt) in enumerate(data):
    y=34-k*12
    text(ax,2,y,lab,'varie','s',ha='left')
    for x,f in zip(xs,m): disc(ax,x,y,3,'resultat' if f else 'fixe')
    text(ax,87,y,cnt,'resultat' if sum(m) else 'limite','s',ha='right')
save(fig,'49-152')
