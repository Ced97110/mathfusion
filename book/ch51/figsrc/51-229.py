import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
box(ax,4,50,62,20,'resultat',fill=False,lw=1.0); text(ax,10,75,r'$D^*$','resultat','m')
text(ax,84,75,'cadran à 7 : ×3','fixe','m',ha='right')
for i,v in enumerate([3,6,2,5,1,4]): disc(ax,10+i*10,60,3.5,'resultat',label=str(v))
disc(ax,78,60,3.5,'fixe',fill=False,label='0')
box(ax,4,15,62,20,'sujet',fill=False,lw=1.0); text(ax,10,40,r'$D^*$','sujet','m')
text(ax,84,40,'cadran à 6 : ×2','fixe','m',ha='right')
disc(ax,20,25,3.5,'sujet',label='3'); disc(ax,78,25,3.5,'limite',fill=False,label='0')
arrow(ax,(23.9,25),(73.6,25),'limite',lw=1.6); text(ax,48,29.5,r'$2\times3=0$','limite','m')
save(fig,'51-229')
