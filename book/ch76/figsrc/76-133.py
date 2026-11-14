import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82); O=(12,10); s=10
P=lambda a,b:(O[0]+a*s,O[1]+b*s)
arrow(ax,P(0,0),P(6.6,0),'fixe',lw=0.7); arrow(ax,P(0,0),P(0,6.6),'fixe',lw=0.7)
text(ax,P(6.6,0)[0],P(6.6,0)[1]-3,r'$x$','fixe','m'); text(ax,P(0,6.6)[0]-3,P(0,6.6)[1],r'$y$','fixe','m')
line(ax,[P(0,5),P(5,0)],'autre',lw=4.5); line(ax,[P(0,5),P(5,0)],'sujet',lw=1.2)
for i in range(6): disc(ax,*P(i,5-i),1.1,'resultat')
text(ax,P(3.9,4.4)[0],P(3.9,4.4)[1],r'$x+y=5$','sujet','m')
text(ax,P(4.4,3.4)[0]+4,P(4.4,3.4)[1],r'$2x+2y=10$','autre','m')
text(ax,66,70,r'$x\times 0=0$','resultat','l')
text(ax,66,63,'une infinité de points','resultat','s')
save(fig,'76-133')
