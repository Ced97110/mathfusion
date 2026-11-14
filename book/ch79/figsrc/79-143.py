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

fig,ax=canvas(64)
xs=[30,52,74]; ys=[14,30,46]; e12=[2,1,0]; e20=[2,0,1]
text(ax,8,58,'exposant','fixe','s')
for e in range(3): text(ax,8,ys[e],str(e),'fixe','s')
for x,p,a,b in zip(xs,[2,3,5],e12,e20):
    text(ax,x,58,f'premier {p}','encre','s')
    line(ax,[(x,ys[0]-4),(x,ys[2]+4)],'fixe')
    for y in ys: line(ax,[(x-1.5,y),(x+1.5,y)],'fixe')
    disc(ax,x-4,ys[a],3,'sujet',label='12',size='s'); disc(ax,x+4,ys[b],3,'autre',label='20',size='s')
text(ax,44,4,'une chaîne par premier','fixe','s')
save(fig,'79-143')
