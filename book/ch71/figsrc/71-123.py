import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,56,r'dans $\{0,\,1\}$ : $x$ tel que $2x=1$ ?','encre','m')
for y,xv,res in [(36,'0',r'$2\times 0=0$'),(18,'1',r'$1+1=0$')]:
    box(ax,4,y,18,9,'sujet',label=rf'$x={xv}$')
    arrow(ax,(23,y+4.5),(33,y+4.5),'varie')
    box(ax,34,y,30,9,'limite',label=res)
    text(ax,76,y+4.5,r'$\neq 1$','limite','l')
text(ax,44,6,r'aucun $x$ : $\frac{1}{2}$ n\'existe pas'.replace("\\'","'"),'limite','m')
save(fig,'71-123')
