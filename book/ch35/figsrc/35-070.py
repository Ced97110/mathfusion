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

fig,ax=canvas(66); O=(14,8); u=50
line(ax,[O,(66,8)],'fixe',lw=0.7); line(ax,[O,(14,60)],'fixe',lw=0.7); arc(ax,O,u,0,90,'fixe',lw=0.8)
cs=lambda a:(math.cos(math.radians(a)),math.sin(math.radians(a)))
U=(O[0]+u*cs(75)[0],O[1]+u*cs(75)[1]); V=(O[0]+u*cs(15)[0],O[1]+u*cs(15)[1]); M=mid(U,V)
line(ax,[U,V],'fixe')
for p,role in ((U,'fixe'),(V,'fixe'),(M,'sujet')):
    line(ax,[p,(p[0],8)],role,lw=0.8,dash=True); line(ax,[p,(14,p[1])],role,lw=0.8,dash=True)
    dot(ax,p,'sujet' if role=='sujet' else 'fixe',1.4)
for p,role in ((U,'fixe'),(V,'fixe'),(M,'sujet')):
    s=('%.4f'%((p[0]-14)/50)).replace('.',','); t=('%.4f'%((p[1]-8)/50)).replace('.',',')
    text(ax,p[0],4.2,s,role,'s'); text(ax,12,p[1],t,role,'s',ha='right')
text(ax,U[0]+3,U[1]+2.5,'U','fixe','m'); text(ax,V[0]+3,V[1]+1.5,'V','fixe','m')
text(ax,M[0]+3,M[1]+2.5,'M','sujet','m',weight='bold')
text(ax,66,54,'M : moyenne des abscisses,\nmoyenne des ordonnées','sujet','s')
save(fig,'35-070')
