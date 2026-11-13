import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,r=22,34,18
disc(ax,cx,cy,r,'sujet',fill=False,lw=1.2)
a1,a2=math.radians(160),math.radians(25)
P=[(cx+r*math.cos(a),cy+r*math.sin(a)) for a in (a1,a2)]
dx,dy=P[1][0]-P[0][0],P[1][1]-P[0][1]; n=math.hypot(dx,dy); dx,dy=dx/n,dy/n
line(ax,[(P[0][0]-6*dx,P[0][1]-6*dy),(P[1][0]+6*dx,P[1][1]+6*dy)],'varie',lw=1.2)
for p in P: disc(ax,p[0],p[1],1.1,'resultat')
text(ax,cx,10,'cercle','sujet','s'); text(ax,cx+4,cy-6,'droite','varie','s',weight='bold')
text(ax,cx,cy+4,'2 points','resultat','s')
x0,w_=52,34
box(ax,x0,46,w_,14,'sujet',label='équation du\n$2^e$ degré',size='s')
arrow(ax,(69,46),(69,40),'varie')
box(ax,x0,26,w_,14,'fixe',label='discriminant\n28',size='s')
arrow(ax,(69,26),(69,20),'varie')
box(ax,x0,6,w_,14,'resultat',label=r'$\sqrt{28}=2\sqrt{7}$',size='s')
arrow(ax,(40,50),(52,53),'varie')
save(fig,'61-017')
