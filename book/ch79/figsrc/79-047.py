import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(56)
y=22
f=numberline(ax,6,80,y,1,8,step=1,labels=False,arrow_right=False)
line(ax,[(6,y),(f(3.5),y)],'varie',3.0); line(ax,[(f(7),y),(80,y)],'resultat',3.0)
disc(ax,f(3.5),y,2.4,'sujet'); disc(ax,f(7),y,2.4,'autre')
text(ax,f(3.5),y-6,'3,5','sujet'); text(ax,f(7),y-6,'7','autre')
text(ax,(6+f(3.5))/2,y-13,'minorants','varie','s'); text(ax,(f(7)+80)/2,y-13,'majorants','resultat','s')
text(ax,f(3.5),y+16,'min = 3,5','resultat'); text(ax,f(7),y+16,'max = 7','resultat')
arrow(ax,(f(3.5),y+13),(f(3.5),y+4),'resultat'); arrow(ax,(f(7),y+13),(f(7),y+4),'resultat')
text(ax,44,50,'deux réels se comparent toujours','fixe','s')
save(fig,'79-047')
