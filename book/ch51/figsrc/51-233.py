import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
xs=[12+12.8*i for i in range(6)]
for x,v in zip(xs,[3,6,2,5,1,4]):
    box(ax,x-5.5,48,11,10,'resultat' if v==1 else 'fixe',label=str(v),lw=1.8 if v==1 else 0.8)
brace(ax,xs[0]-6,xs[5]+6,59,'fixe',label='arrivées de ×3',down=False)
disc(ax,30,24,3.5,'resultat',label='5')
link((30,24),(xs[4],47.6),3.5,0,'varie',1.4); text(ax,53,31,r'$\times3$','varie','m')
text(ax,24,8,r'$3\times5=1$','resultat','m'); text(ax,66,8,r'$5\times3=1$','resultat','m')
save(fig,'51-233')
