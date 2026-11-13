import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,28,60,32,11,'sujet',label=r'$x=\pm 1$',size='l')
text(ax,44,76,'deux choix en un seul signe','fixe','s')
for cx,a,x,pr in [(21,'5','1',r'$5\times 1=5$'),(67,'-5','-1',r'$(-5)\times(-1)=5$')]:
    arrow(ax,(44,52) if False else (44+(cx-44)*0.3,59.5),(cx,46),'varie')
    box(ax,cx-19,34,38,11,'autre',label=r'$a=%s$ : $x=%s$'%(a,x),size='s')
    arrow(ax,(cx,33),(cx,25),'varie')
    box(ax,cx-19,12,38,12,'resultat',label=pr,size='s')
text(ax,44,5,'un seul choix à la fois','limite','s')
save(fig,'05-103')
