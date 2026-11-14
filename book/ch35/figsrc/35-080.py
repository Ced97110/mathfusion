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

fig,ax=canvas(68)
text(ax,22,63,'cas général','fixe','m',weight='bold'); text(ax,66,63,'exemple chiffré','fixe','m',weight='bold')
L=[(2,'sujet',r'$a\sin x+b\cos x=c$'),(2,'varie',r'$R\sin(x+\alpha)=c$'),(2,'resultat',r'$\sin z=c/R$')]
Rr=['3 sin x + 4 cos x = 3','5 sin(x + α) = 3','sin z = 3/5 = 0,6']
for i,y in enumerate((44,24,4)):
    x,role,lab=L[i]; box(ax,2,y,40,12,role,label=lab); box(ax,46,y,40,12,role,label=Rr[i])
for xa,lab1,lab2 in ((22,r'$R=\sqrt{a^2+b^2}$','z = x + α, ÷ R'),(66,'R = 5','z = x + α, ÷ 5')):
    arrow(ax,(xa,44),(xa,36.5),'fixe'); arrow(ax,(xa,24),(xa,16.5),'fixe')
    text(ax,xa+3.5,40,lab1,'fixe','s',ha='left'); text(ax,xa+3.5,20,lab2,'fixe','s',ha='left')
save(fig,'35-080')
