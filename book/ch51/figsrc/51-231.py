import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(75)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
xs=[12+12.8*i for i in range(6)]
brace(ax,xs[0]-4.5,xs[5]+4.5,62,'sujet',label='6 départs différents',down=False)
brace(ax,xs[0]-5.5,xs[5]+5.5,14,'resultat',label='6 places, toutes occupées',down=True)
for i in range(6):
    j=(3*(i+1))%7-1
    link((xs[i],56),(xs[j],23.4),3.5,0,'fixe',0.9)
for i in range(6):
    disc(ax,xs[i],56,3.5,'sujet',label=str(i+1)); box(ax,xs[i]-5,14,10,9,'resultat',label=str(i+1))
save(fig,'51-231')
