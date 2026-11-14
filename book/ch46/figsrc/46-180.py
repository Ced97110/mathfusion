import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pos(cx,cy,r,k,n,a0=90):
    a=math.radians(a0-360*k/n); return (cx+r*math.cos(a), cy+r*math.sin(a))
def edge(p,q,d):
    vx,vy=q[0]-p[0],q[1]-p[1]; L=math.hypot(vx,vy); return (p[0]+vx/L*d,p[1]+vy/L*d)
def link(ax,p,q,dr,role,curve=0.0):
    arrow(ax,edge(p,q,dr+0.2),edge(q,p,dr+0.2),role,curve=curve)
def loop(ax,p,dr,ang,role='fixe'):
    a=math.radians(ang); R=1.9; c=(p[0]+(dr+R-0.4)*math.cos(a), p[1]+(dr+R-0.4)*math.sin(a))
    ax.add_patch(Circle(c,R,ec=COL[role],fc='none',lw=0.8,zorder=3))
def cyc(ax,cx,cy,r,nums,role,dr=2.6,size='m'):
    n=len(nums)
    if n==1:
        disc(ax,cx,cy,dr,role,label=str(nums[0]),size=size); loop(ax,(cx,cy),dr,90,role); return
    P=[(cx-r,cy),(cx+r,cy)] if n==2 else [pos(cx,cy,r,k,n) for k in range(n)]
    for k in range(n): link(ax,P[k],P[(k+1)%n],dr,role,curve=-0.3 if n==2 else 0)
    for k in range(n): disc(ax,P[k][0],P[k][1],dr,role,label=str(nums[k]),size=size)
def tri(ax,cx,cy,r,m,role,labels=False,dr=2.6,fixrole='fixe',loops=False):
    P={i:pos(cx,cy,r,i-1,3) for i in (1,2,3)}
    for i in (1,2,3):
        j=m[i]
        if j!=i: link(ax,P[i],P[j],dr,role,curve=0.35 if m[j]==i else 0)
    for i in (1,2,3):
        rr=role if m[i]!=i else fixrole
        disc(ax,P[i][0],P[i][1],dr,rr,label=str(i) if labels else None)
        if loops and m[i]==i: loop(ax,P[i],dr,90-120*(i-1),rr)
    return P

fig,ax=canvas(58)
poly(ax,[(6,28),(6,52),(30,52),(30,28)],'sujet')
for (x,y,l) in ((6,52,'1'),(30,52,'2'),(30,28,'3'),(6,28,'4')): disc(ax,x,y,3,'sujet',label=l,size='s')
text(ax,18,20,'symétries du carré','sujet','s')
box(ax,37,10,49,44,'fixe',fill=False)
text(ax,61.5,48,r'$S_4$ : 24 mélanges','fixe','s')
for r_ in range(4):
    for c in range(6):
        disc(ax,44+6.3*c,22+6.3*r_,1.8,'sujet' if c<2 else 'fixe')
box(ax,40,19,16,24,'sujet',fill=False,lw=1.1)
text(ax,48,14,'8 mélanges','sujet','s')
arrow(ax,(33,40),(39.5,40),'sujet')

save(fig,'46-180')
