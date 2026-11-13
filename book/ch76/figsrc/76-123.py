import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
u=14; o=(14,14)
P=lambda x,y:(o[0]+x*u,o[1]+y*u)
arrow(ax,P(0,0),P(4.1,0),'fixe',lw=0.8); arrow(ax,P(0,0),P(0,2.1),'fixe',lw=0.8)
text(ax,P(4.1,0)[0],P(0,0)[1]-3,r'$x$','fixe','m'); text(ax,P(0,0)[0]-3,P(0,2.1)[1],r'$y$','fixe','m')
line(ax,[P(-0.3,1.65),P(3.4,-0.2)],'limite',lw=2)
for (a,b,l) in [(1,1,r'$(1,1)$'),(3,0,r'$(3,0)$')]:
    disc(ax,*P(a,b),1.4,'resultat'); text(ax,P(a,b)[0],P(a,b)[1]+4.5,l,'resultat','s')
text(ax,50,40,r'$x+2y=3$','limite','m'); text(ax,50,33,r'$2x+4y=6$','limite','m')
text(ax,44,68,r'$\det=1\times4-2\times2=0$','limite','l')
text(ax,44,60,'division par 0 impossible','limite','m')
text(ax,44,5,'deux solutions, donc pas une seule','fixe','m')
save(fig,'76-123')
