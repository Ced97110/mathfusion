import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
u=3
def par(o,A,B,role):
    pts=[(0,0),A,(A[0]+B[0],A[1]+B[1]),B]
    poly(ax,[(o[0]+x*u,o[1]+y*u) for x,y in pts],role)
o1,o2=(8,12),(50,12)
par(o1,(1,2),(1,1),'sujet'); par(o2,(5,8),(1,1),'resultat')
text(ax,o1[0]-2,o1[1]+3,r'$a$','sujet','s'); text(ax,o1[0]+5,o1[1]-2,r'$b$','autre','s')
text(ax,o2[0]+4,o2[1]+14,r'$c$','resultat','s'); text(ax,o2[0]+5,o2[1]-2,r'$b$','autre','s')
arrow(ax,(24,26),(46,26),'varie'); text(ax,35,30,r'$\times\,x$','varie','l')
text(ax,14,4,r'$a\wedge b=-1$','sujet','m'); text(ax,64,4,r'$c\wedge b=-3$','resultat','m')
text(ax,44,56,r'$x\,(a\wedge b)=c\wedge b$','encre','l')
save(fig,'76-118')
