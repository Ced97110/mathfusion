import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,16,52,56,10,'sujet',label=r'$(x+2)(x+3)=0$',size='l')
arrow(ax,(32,52),(22,42),'varie'); arrow(ax,(56,52),(66,42),'varie')
box(ax,2,30,40,10,'sujet',label=r'$x+2=0$',size='m'); box(ax,46,30,40,10,'autre',label=r'$x+3=0$',size='m')
arrow(ax,(22,30),(22,18),'varie'); arrow(ax,(66,30),(66,18),'varie')
box(ax,2,6,40,10,'resultat',label=r'$x=-2$',size='m'); box(ax,46,6,40,10,'resultat',label=r'$x=-3$',size='m')
text(ax,44,46,'deux équations','varie','s')
save(fig,'18-112')
