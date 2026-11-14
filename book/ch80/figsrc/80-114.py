import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,8,70,50,0,6,labels=True)
for v,y in [(2,0),(5,0)]:
    disc(ax,f(v),50,1.6,'varie'); arrow(ax,(f(v),46),(f(v),30),'varie')
box(ax,f(2)-17,18,34,12,'sujet',label=r'$(1,2,0)$',size='s'); box(ax,f(5)-17+ (0 if f(5)+17<86 else 86-f(5)-17),18,34,12,'sujet',label=r'$(1,5,0)$',size='s')
text(ax,44,58,'scalaires','varie','s'); text(ax,44,10,'un point par scalaire','sujet','s')
save(fig,'80-114')
