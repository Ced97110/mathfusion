import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
y=26
f=numberline(ax,6,82,y,-6,6,labels=False,arrow_right=False)
arrow(ax,(f(0),y+1.5),(f(5),y+1.5),'varie',curve=-0.45)
arrow(ax,(f(0),y+1.5),(f(-5),y+1.5),'varie',curve=0.45)
disc(ax,f(0),y,1.5,'fixe'); disc(ax,f(5),y,1.8,'sujet'); disc(ax,f(-5),y,1.8,'sujet')
text(ax,f(0),y-4,'0','fixe','s'); text(ax,f(5),y-4,'5','sujet','s'); text(ax,f(-5),y-4,r'$-5$','sujet','s')
text(ax,f(2.5),37,'5 pas','varie','s'); text(ax,f(-2.5),37,'5 pas','varie','s')
text(ax,f(5),13,r'$|5|=5$','sujet','m'); text(ax,f(-5),13,r'$|-5|=5$','sujet','m')
text(ax,44,49,r'$|b|$ : pas jusqu’à 0','sujet','l')
save(fig,'05-031')
