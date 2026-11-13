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

fig,ax=canvas(80); O=(44,38); r=28
arc(ax,O,r,0,360,'fixe',lw=0.9)
U=(O[0]+r,O[1]); V=(O[0]-r,O[1])
line(ax,[U,V],'sujet',lw=1.5); arc(ax,O,14,0,180,'varie',lw=1.3)
for p in (U,V): dot(ax,p,'sujet',1.4)
disc(ax,O[0],O[1],2.3,'resultat')
text(ax,U[0]+4,U[1]+3,'U','sujet','m',weight='bold'); text(ax,U[0]+1,U[1]-4.5,'(1 ; 0)','sujet','s')
text(ax,V[0]-4,V[1]+3,'V','sujet','m',weight='bold'); text(ax,V[0]-1,V[1]-4.5,'(−1 ; 0)','sujet','s')
text(ax,O[0],O[1]+6,'M = O','resultat','m',weight='bold'); text(ax,O[0],O[1]-6,'diamètre','sujet','s')
text(ax,O[0],O[1]+19,'180°','varie','m')
text(ax,44,74,r'$\cos 0^\circ+\cos 180^\circ=1-1=0$','resultat','m')
text(ax,44,5,r'$\cos 90^\circ=0$','varie','m')
save(fig,'35-075')
