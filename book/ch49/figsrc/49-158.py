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
fig,ax=canvas(44)
c=3.4; cases=[(4,2,8,12),(1,4,4,34),(4,1,4,56),(2,2,4,78)]
for o,s,g,cx in cases:
    x=cx-o*c/2
    for i in range(o):
        for j in range(s): box(ax,x+i*c,18+j*c,c,c,'sujet',lw=0.5,r=0.3)
    text(ax,cx,11,rf'${o}\times {s} = {g}$','encre','s')
brace(ax,2,22,34,'fixe',label=r'carré, $|G|$ = 8',down=False)
brace(ax,26,86,34,'fixe',label=r'rotations, $|G|$ = 4',down=False)
text(ax,22,4,'colonnes = orbite','sujet','s'); text(ax,64,4,'lignes = stabilisateur','varie','s')
save(fig,'49-158')
