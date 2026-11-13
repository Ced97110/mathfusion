import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84); O=(14,10); s=8
P=lambda a,b:(O[0]+a*s,O[1]+b*s)
arrow(ax,P(0,0),P(8.8,0),'fixe',lw=0.7); arrow(ax,P(0,0),P(0,8.8),'fixe',lw=0.7)
text(ax,P(8.8,0)[0],P(8.8,0)[1]-3,r'$x$','fixe','m'); text(ax,P(0,8.8)[0]-3,P(0,8.8)[1],r'$y$','fixe','m')
line(ax,[P(0,5),P(5,0)],'sujet',lw=1.6); line(ax,[P(0,8),P(8,0)],'autre',lw=1.6)
text(ax,26,24,r'$x+y=5$','sujet','m')
text(ax,P(5.4,2.6)[0]+6,P(5.4,2.6)[1]+3,r'$x+y=8$','autre','m')
text(ax,66,70,'jamais ensemble','limite','m')
text(ax,66,63,r'$x\times 0=-3$','limite','l')
save(fig,'76-132')
