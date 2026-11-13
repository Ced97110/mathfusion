import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
pts=[(10,32),(20,34),(29,30),(12,18),(22,22),(30,14)]
for x,y in pts:
    disc(ax,x,y,2.5,'fixe')
    disc(ax,x+48,y,2.5,'fixe')
text(ax,19,44,'6 élèves, un par un','fixe','s')
arrow(ax,(36,24),(48,24),'varie')
text(ax,42,29,'rassembler','varie','s')
box(ax,50,8,36,32,'sujet',fill=False,lw=1.3,r=3)
text(ax,68,44,'la classe : 1 objet','sujet','m')
text(ax,68,4,'« la classe a décidé »','resultat','s')
save(fig,'01-032')
