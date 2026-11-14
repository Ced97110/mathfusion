import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
cx,cy,u=24,28,9
disc(ax,cx,cy,2*u,'sujet',fill=False,lw=1.1)
line(ax,[(cx-2.5*u,cy+3*u),(cx+2.5*u,cy+3*u)],'limite',lw=1.3)
text(ax,cx,cy,r'$x^2+y^2=4$','sujet','s')
text(ax,9,cy+3*u+4.5,r'$y=3$','limite','s')
text(ax,cx,cy+2.5*u+0.2,'aucun point commun','limite','s')
ys=[54,40,26,12]
items=[(r'$x^2+3^2=4$','fixe'),(r'$x^2=-5$','varie'),('aucun $x$ réel','limite'),('aucun point produit','limite')]
for (l,r),y in zip(items,ys): box(ax,50,y,36,10,r,label=l,size='s')
for i in range(3): arrow(ax,(68,ys[i]),(68,ys[i+1]+10),'fixe')
save(fig,'61-181')
