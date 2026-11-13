import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
u=10
A=(14,10); B=(A[0]+4*u,A[1]); C=(A[0],A[1]+3*u)
poly(ax,[A,B,C],'fixe',fill=False)
line(ax,[B,C],'sujet',lw=2.4)
line(ax,[A,B],'fixe',lw=1.4); line(ax,[A,C],'fixe',lw=1.4)
line(ax,[(A[0]+2.4,A[1]),(A[0]+2.4,A[1]+2.4),(A[0],A[1]+2.4)],'encre',lw=0.7)
text(ax,A[0]+2*u,A[1]-3,'4','fixe','m'); text(ax,A[0]-3,A[1]+1.5*u,'3','fixe','m')
text(ax,38,32,'5 : hypoténuse','sujet','s',ha='left')
text(ax,A[0]+3,A[1]+11,'angle droit','encre','s',ha='left')
arrow(ax,(A[0]+6,A[1]+8),(A[0]+3.2,A[1]+3.4),'varie')
text(ax,44,52,'$5^2=3^2+4^2$','resultat','m')
save(fig,'22-129')
