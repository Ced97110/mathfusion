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

def wave(shift,name):
    fig,ax=canvas(66); x0,x1,yb,y0,A=14,80,8,36,14
    tx=lambda t:x0+t/360*(x1-x0); ty=lambda v:y0+A*v/5
    numberline(ax,x0,x1,yb,0,360,step=90,labels=(name=='35-076'),arrow_right=False)
    for s in (5,-5): line(ax,[(x0,ty(s)),(x1,ty(s))],'fixe',lw=0.6,dash=True)
    line(ax,[(x0,y0),(x1,y0)],'fixe',lw=0.6)
    line(ax,[(tx(t),ty(5*math.sin(math.radians(t+shift)))) for t in range(0,361,4)],'sujet',lw=1.5)
    for s,l in ((5,'5'),(0,'0'),(-5,'−5')): text(ax,11.5,ty(s),l,'fixe','s',ha='right')
    return fig,ax,tx,ty

fig,ax,tx,ty=wave(53.13,'35-077')
for t,s in ((36.87,5),(216.87,-5)):
    line(ax,[(tx(t),ty(s)),(tx(t),8)],'resultat',lw=0.6,dash=True); disc(ax,tx(t),ty(s),1.5,'resultat')
    text(ax,tx(t),3.6,('%.2f°'%t).replace('.',','),'resultat','s',weight='bold')
text(ax,tx(36.87)+9,ty(5)+4,'maximum 5','resultat','m',weight='bold'); text(ax,tx(216.87),ty(-5)-4,'minimum −5','resultat','m',weight='bold')
text(ax,50,61,r'$5\,\sin(x+53{,}13^\circ)$','sujet','l'); text(ax,83,8,'x','fixe','s')
save(fig,'35-077')
