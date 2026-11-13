import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,19,64,'preuve','sujet','m'); text(ax,69,64,'exemple (7) et 3','autre','m')
L=[r'$a\notin M$',r'$ra+m\in I$',r'$1\in I$']
R=[r'$3\notin(7)$',r'$5\times3+(-14)$',r'$5\times3-14=1$']
for y,l,r in zip((44,28,12),L,R):
    box(ax,2,y,34,10,'sujet',label=l)
    arrow(ax,(37,y+5),(51,y+5),'fixe')
    box(ax,52,y,34,10,'autre',label=r)
for y in (44,28):
    arrow(ax,(19,y),(19,y-6),'varie'); arrow(ax,(69,y),(69,y-6),'varie')
save(fig,'52-105')
