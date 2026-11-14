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

fig,ax=canvas(64)
text(ax,44,60,r'ordre $r$ : $r$ éléments engendrés','sujet','m')
rows=[(48,r'$S_3$ : 6',None),(34,'ordre 1',1),(20,'ordre 2',2),(6,'ordre 3',3)]
for y,lab,n in rows:
    text(ax,3,y+4,lab,'fixe' if n is None else 'sujet','s',ha='left')
    for k in range(6):
        x=30+9.5*k
        if n is None: box(ax,x,y,8,8,'fixe',r=0.4)
        elif k<n: box(ax,x,y,8,8,'sujet',r=0.4)
        else: box(ax,x,y,8,8,'limite',fill=False,dash=True,r=0.4)

save(fig,'46-191')
