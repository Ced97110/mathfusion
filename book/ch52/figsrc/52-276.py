import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$(a)=\{xa\mid x\in R\}$, avec $a=2$','sujet','m')
for i in range(6):
    x=5+i*13.4
    box(ax,x,40,11,9,'sujet',label=r'$x=%d$'%i,size='s')
    arrow(ax,(x+5.5,40),(x+5.5,31),'varie')
    box(ax,x,21,11,10,'varie',label=str((2*i)%6))
text(ax,44,10,r'$(2)=\{0,\,2,\,4\}$','resultat','m')
save(fig,'52-276')
