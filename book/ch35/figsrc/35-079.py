import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role='fixe',lw=0.9,dash=False):
    line(ax,[P(c,r,a0+(a1-a0)*i/48) for i in range(49)],role,lw,dash)
def mid(p,q): return ((p[0]+q[0])/2,(p[1]+q[1])/2)
def ra(ax,m,d1,d2,s=1.8,role='fixe'):
    n1=math.hypot(*d1); n2=math.hypot(*d2); u=(d1[0]/n1,d1[1]/n1); v=(d2[0]/n2,d2[1]/n2)
    line(ax,[(m[0]+s*u[0],m[1]+s*u[1]),(m[0]+s*(u[0]+v[0]),m[1]+s*(u[1]+v[1])),(m[0]+s*v[0],m[1]+s*v[1])],role,lw=0.7)
def tick(ax,p,q,n=1,role='fixe',s=1.2):
    m=mid(p,q); dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; nx,ny=-uy,ux
    for i in range(n):
        o=(i-(n-1)/2)*1.1
        c=(m[0]+ux*o,m[1]+uy*o); line(ax,[(c[0]-nx*s,c[1]-ny*s),(c[0]+nx*s,c[1]+ny*s)],role,lw=0.8)
def dot(ax,p,role,r=1.1): disc(ax,p[0],p[1],r,role)

fig,ax=canvas(76); O=(26,44); u=11
line(ax,[(4,44),(84,44)],'fixe',lw=0.6); line(ax,[(26,6),(26,64)],'fixe',lw=0.6)
Pt=(O[0]+u,O[1]-3*u)
line(ax,[O,Pt],'resultat',lw=1.5)
line(ax,[Pt,(Pt[0],44)],'fixe',lw=0.7,dash=True); line(ax,[Pt,(26,Pt[1])],'fixe',lw=0.7,dash=True)
arc(ax,O,14,0,-71.57,'varie',lw=1.5)
dot(ax,Pt,'sujet',1.5)
text(ax,Pt[0],48,'1','fixe','s'); text(ax,23.5,Pt[1],'−3','fixe','s',ha='right')
text(ax,Pt[0],Pt[1]-4.5,'(1 ; −3)','sujet','m',weight='bold')
q=P(O,22,-36); text(ax,q[0],q[1],'α ≈ −1,249 rad','varie','s',ha='left')
text(ax,Pt[0]+4,20,'R = √10 ≈ 3,162','resultat','s',ha='left',weight='bold')
text(ax,68,36,'4e quadrant','fixe','s')
text(ax,44,70,r'$\sin x-3\cos x=\sqrt{10}\,\sin(x-1{,}249)$','encre','m')
save(fig,'35-079')
