import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,u=24,30,9
disc(ax,cx,cy,2*u,'sujet',fill=False,lw=1.1)
line(ax,[(cx-2.5*u,cy+2*u),(cx+2.5*u,cy+2*u)],'varie',lw=1.3)
disc(ax,cx,cy+2*u,1.3,'resultat')
text(ax,cx,cy,r'$x^2+y^2=4$','sujet','s')
text(ax,9,cy+2*u+4.5,r'$y=2$','varie','s')
text(ax,34,cy+2*u+8,'un seul point','resultat','s')
ys=[46,30,14]
for (l,r),y in zip([(r'$\Delta=0$','varie'),(r'$\sqrt{0}=0$','fixe'),('aucun étage ajouté','resultat')],ys):
    box(ax,50,y,36,10,r,label=l,size='s')
for i in range(2): arrow(ax,(68,ys[i]),(68,ys[i+1]+10),'fixe')
save(fig,'61-180')
