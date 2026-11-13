import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
u=3
def par(o,A,B,role):
    pts=[(0,0),A,(A[0]+B[0],A[1]+B[1]),B]
    poly(ax,[(o[0]+x*u,o[1]+y*u) for x,y in pts],role)
o0,o1,o2=(8,14),(35,14),(58,14)
arrow(ax,o0,(o0[0]+3,o0[1]+6),'fixe',lw=1.3)
par(o1,(1,2),(1,1),'sujet'); par(o2,(1,2),(5,8),'resultat')
text(ax,15,24,r'$a$','fixe','s')
text(ax,14,6,r'$a\wedge a=0$','fixe','m'); text(ax,38,6,r'$a\wedge b=-1$','sujet','m'); text(ax,68,6,r'$a\wedge c=-2$','resultat','m')
arrow(ax,(46,28),(60,28),'varie'); text(ax,53,32,r'$\times\,y$','varie','l')
text(ax,44,52,r'$y=\dfrac{-2}{-1}=2$','resultat','l')
save(fig,'76-121')
