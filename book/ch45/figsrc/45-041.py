import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,16,64,r'$b=1$','limite','m',weight='bold')
for y,a in [(50,r'$1^3$'),(36,r'$1^5$'),(22,r'$1^{-2}$')]:
    box(ax,4,y-5,24,10,'sujet',label=a,size='m')
    arrow(ax,(31,y),(60,36+(y-36)*0.3),'limite')
disc(ax,70,36,7,'limite',label=r'$1$',size='l')
text(ax,70,25,'un seul nombre','limite','s')
text(ax,44,8,'on ne retrouve plus le départ','limite','s')
save(fig,'45-041')
