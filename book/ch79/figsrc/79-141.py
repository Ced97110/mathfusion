import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
LAB={'a':r'$a$','b':r'$b$','c':r'$c$','x':r'$x$','y':r'$y$','z':r'$z$'}
def _pl(P,ox,oy,k): return {n:(ox+x*k,oy+y*k) for n,(x,y) in P.items()}
def N5(ox,oy,k=1.0): return _pl({'0':(0,0),'1':(0,40),'a':(-14,20),'b':(14,13),'c':(14,27)},ox,oy,k)
def M3(ox,oy,k=1.0): return _pl({'0':(0,0),'1':(0,40),'x':(-14,20),'y':(0,20),'z':(14,20)},ox,oy,k)
N5E=[('0','a'),('a','1'),('0','b'),('b','c'),('c','1')]
M3E=[('0','x'),('0','y'),('0','z'),('x','1'),('y','1'),('z','1')]
def hasse(ax,pos,edges,roles,edge_role='fixe',r=3.0,lw=0.9):
    for a,b in edges:
        (x0,y0),(x1,y1)=pos[a],pos[b]; d=math.hypot(x1-x0,y1-y0); ux,uy=(x1-x0)/d,(y1-y0)/d
        line(ax,[(x0+ux*r,y0+uy*r),(x1-ux*r,y1-uy*r)],edge_role,lw)
    for n,p in pos.items():
        disc(ax,p[0],p[1],r,roles.get(n,'fixe') if isinstance(roles,dict) else roles,label=LAB.get(n,n),size='s')

fig,ax=canvas(54)
f=numberline(ax,8,76,40,2,8,step=1)
for v,n,role in ((3,'b','varie'),(5,'a','sujet'),(7,'c','autre')): disc(ax,f(v),40,2.2,role,label=rf'${n}$')
box(ax,2,8,41,10,'sujet',label=r'$a\wedge(b\vee c)=5\wedge7=5$',size='s'); box(ax,45,8,41,10,'varie',label=r'$(a\wedge b)\vee(a\wedge c)=3\vee5=5$',size='s')
arrow(ax,(22,18.8),(f(5)-1,31),'resultat'); arrow(ax,(66,18.8),(f(5)+1,31),'resultat')
text(ax,44,50,r'$\vee$ = max, $\wedge$ = min','fixe','s')
save(fig,'79-141')
