import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(105)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
xs=[12+12.8*i for i in range(6)]
brace(ax,xs[0]-4.5,xs[5]+4.5,98,'sujet',label='6 départs distincts',down=False)
for x in xs:
    disc(ax,x,92,3,'sujet'); arrow(ax,(x,88.7),(x,80.4),'fixe',lw=0.9); box(ax,x-4,72,8,8,'resultat')
brace(ax,xs[0]-5,xs[5]+5,72,'resultat',label='6 places, aucune vide',down=True)
line(ax,[(4,56),(84,56)],'fixe',dash=True)
text(ax,4,50,r'entiers : $x\mapsto 2x$','limite','m',ha='left')
for k in range(3,6): disc(ax,xs[k],42,1.2,'fixe')
for i in range(3): disc(ax,xs[i],42,3,'sujet',label=str(i+1))
for i in range(6):
    hit=(i+1)%2==0
    box(ax,xs[i]-4.5,20,9,9,'resultat' if hit else 'limite',fill=hit,dash=not hit,label=str(i+1))
for i in range(3): link((xs[i],42),(xs[2*(i+1)-1],29.5),3,0,'limite',1.0)
text(ax,4,12,'1 n’est jamais atteint','limite','s',ha='left')
save(fig,'51-232')
