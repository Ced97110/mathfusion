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

fig,ax=canvas(72)
box(ax,3,36,36,26,'sujet'); box(ax,49,36,36,26,'resultat')
text(ax,21,57,'dans un cycle','sujet','s'); text(ax,67,57,'dans le mélange','resultat','s')
text(ax,44,48,'=','encre','l')
for x0,role in ((21,'sujet'),(67,'resultat')):
    a=(x0-9,47); b=(x0+9,47)
    link(ax,a,b,3,role); disc(ax,*a,3,role,label='1'); disc(ax,*b,3,role,label='3')
text(ax,21,40,'3 suit 1','sujet','m'); text(ax,67,40,r'$\sigma(1)=3$','resultat','m')
box(ax,3,4,82,26,'limite',fill=True)
a=(14,17); b=(40,17)
link(ax,a,b,3,'limite'); disc(ax,*a,3,'limite',label='1'); disc(ax,*b,3,'limite',label='5')
cx=27; line(ax,[(cx-2,19.5),(cx+2,14.5)],'limite',lw=1.4); line(ax,[(cx-2,14.5),(cx+2,19.5)],'limite',lw=1.4)
text(ax,64,17,'« 5 suit 1 » : faux','limite','m')

save(fig,'46-177')
