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

fig,ax=canvas(66)
xc=48; pitch=4.636*9/72*25.4; hw=1.5*pitch
S=lambda a,b,c: rf'${a}\qquad\qquad {b}\qquad\qquad {c}$'
text(ax,13,58,'premiers','fixe','s'); text(ax,xc,58,S(2,3,5),'fixe','l')
R=[(44,'sujet','12',(2,1,0)),(33,'autre','20',(2,0,1)),(17,'resultat',r'$\wedge$ : min',(2,0,0)),(6,'resultat',r'$\vee$ : max',(2,1,1))]
for y,role,lab,v in R:
    box(ax,2,y,22,9,role,label=lab,size='s'); box(ax,xc-hw,y,2*hw,9,role)
    for s in (-1,1): line(ax,[(xc+s*pitch/2,y+1),(xc+s*pitch/2,y+8)],'fixe',lw=0.5)
    text(ax,xc,y+4.5,S(*v),role,'l')
text(ax,79,21.5,'PGCD = 4','resultat','s'); text(ax,79,10.5,'PPCM = 60','resultat','s')
arrow(ax,(xc,32.5),(xc,26.5),'varie')
save(fig,'79-144')
