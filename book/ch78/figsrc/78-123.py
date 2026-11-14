import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
k=1.4; x0=8
box(ax,x0,32,50*k,11,'autre',label=r'$Q(u)\,Q(v)=5\times10=50$')
box(ax,x0,12,46*k,11,'sujet',label=r'$Q(u\times v)=46$')
box(ax,x0+46*k,12,4*k,11,'limite',dash=True)
text(ax,x0+48*k,5,'il manque 4','limite','m')
arrow(ax,(x0+48*k,7.5),(x0+48*k,11),'limite')
text(ax,x0+25*k,47,r'$46\neq50$','limite','l')
save(fig,'78-123')
