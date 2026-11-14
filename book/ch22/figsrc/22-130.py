import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
u=4.5
a=(8,24)
poly(ax,[a,(a[0]+4*u,a[1]),(a[0],a[1]+3*u)],'resultat')
line(ax,[(a[0]+2.4,a[1]),(a[0]+2.4,a[1]+2.4),(a[0],a[1]+2.4)],'encre',lw=0.7)
text(ax,a[0]+2*u,a[1]-2.8,'4','resultat','s'); text(ax,a[0]-2.2,a[1]+1.5*u,'3','resultat','s')
text(ax,a[0]+2.6*u+2.8,a[1]+1.8*u,'5','resultat','s')
text(ax,a[0]+9,58,'angle droit','resultat','s')
text(ax,a[0]+9,14,'$9+16=25$','resultat','m')
b=(54,24); s=3*u
pts=[b,(b[0]+s,b[1]),(b[0]+s/2,b[1]+s*0.866)]
poly(ax,pts,'limite')
text(ax,b[0]+s/2,b[1]-2.8,'3','limite','s'); text(ax,b[0]+s/4-3,b[1]+s*0.43+1,'3','limite','s'); text(ax,b[0]+3*s/4+3,b[1]+s*0.43+1,'3','limite','s')
text(ax,b[0]+s/2+3,58,'pas d’angle droit','limite','s')
text(ax,b[0]+s/2+3,14,'$9+9=18\\neq 9$','limite','m')
line(ax,[(44,8),(44,62)],'fixe',dash=True)
save(fig,'22-130')
