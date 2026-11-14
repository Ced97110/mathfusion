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

fig,ax=canvas(78)
text(ax,14,72,'(1 3 5)','sujet','m'); text(ax,33,72,'(3 4 7)','varie','m'); text(ax,46,72,'=','encre','m'); text(ax,68,72,'(1 3 4 7 5)','resultat','m')
text(ax,14,66,'longueur 3','sujet','s'); text(ax,33,66,'longueur 3','varie','s')
cyc(ax,44,32,20,[1,3,4,7,5],'resultat')
text(ax,44,32,'un seul cycle\nde longueur 5','resultat','s')

save(fig,'46-184')
