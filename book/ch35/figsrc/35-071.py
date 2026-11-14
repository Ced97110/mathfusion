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

fig,ax=canvas(68); O=(44,60); L=46
U=(O[0]-L*0.5,O[1]-L*math.sqrt(3)/2); V=(O[0]+L*0.5,U[1]); M=(O[0],U[1])
line(ax,[O,U],'sujet',lw=1.4); line(ax,[O,V],'sujet',lw=1.4); line(ax,[U,V],'fixe',lw=1.2)
line(ax,[O,M],'resultat',lw=1.4)
tick(ax,O,U,2,'sujet'); tick(ax,O,V,2,'sujet'); tick(ax,U,M,1,'fixe'); tick(ax,M,V,1,'fixe')
ra(ax,M,(0,1),(1,0),2.4,'resultat')
arc(ax,O,14,-120,-90,'varie',lw=1.2); arc(ax,O,14,-90,-60,'varie',lw=1.2)
for p in (O,U,V,M): dot(ax,p,'sujet' if p in (O,U,V) else 'resultat',1.2)
text(ax,O[0],O[1]+4,'O','sujet','m'); text(ax,U[0]-3.5,U[1]-1,'U','sujet','m'); text(ax,V[0]+3.5,V[1]-1,'V','sujet','m')
text(ax,M[0],M[1]-4,'M','resultat','m',weight='bold')
q=P(O,22,-106); text(ax,q[0],q[1],'30°','varie','s'); q=P(O,22,-74); text(ax,q[0],q[1],'30°','varie','s')
text(ax,M[0]+6,M[1]+5,'90°','resultat','s')
text(ax,O[0]-2,32,'OM = 0,866','resultat','s',ha='right')
text(ax,24,5,'OU = OV','sujet','m'); text(ax,64,5,'UM = MV','fixe','m')
save(fig,'35-071')
