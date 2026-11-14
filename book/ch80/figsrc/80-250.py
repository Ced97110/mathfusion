import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
for cx,rule,vals,gv in ((23,r'$f(y)=y$',(6,2,3,1),12),(65,r'$f(y)=1$',(1,1,1,1),4)):
    text(ax,cx,74,rule,'varie','m')
    pos={1:(cx,26),2:(cx-10.5,43),3:(cx+10.5,43),6:(cx,60)}
    for a,b in ((1,2),(1,3),(2,6),(3,6)): line(ax,[pos[a],pos[b]],'fixe')
    for (n,(x,y)),v in zip(((6,pos[6]),(2,pos[2]),(3,pos[3]),(1,pos[1])),vals):
        box(ax,x-9,y-4.5,18,9,'sujet',label=r'$f$(%d) = %d'%(n,v),size='s')
    text(ax,cx,10,r'$g$(6) = %d'%gv,'resultat','m')
[l.set_zorder(1.5) for l in ax.lines]
save(fig,'80-250')
