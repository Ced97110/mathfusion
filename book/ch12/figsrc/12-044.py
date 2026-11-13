import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'trois cas','sujet','m')
for i,(a,b) in enumerate([(r'$=$',r'$\neq$'),(r'$<$',r'$\geq$'),(r'$>$',r'$\leq$')]):
    x=5+i*28
    box(ax,x,36,22,13,'sujet',label=a,size='l')
    box(ax,x,10,22,13,'autre',label=b,size='l')
    arrow(ax,(x+11,35),(x+11,24),'varie',both=True)
text(ax,44,4,'leurs contraires','autre','m')
save(fig,'12-044')
