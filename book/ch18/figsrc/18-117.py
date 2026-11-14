import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,2,34,22,10,'sujet',label=r'$x^2-2$',size='m'); arrow(ax,(24,39),(46,39),'varie'); text(ax,35,44,r'carré $=2$','varie','s')
box(ax,46,34,40,10,'resultat',label=r'$(x+\sqrt{2})(x-\sqrt{2})$',size='s')
box(ax,2,10,22,10,'sujet',label=r'$x^2+1$',size='m'); arrow(ax,(24,15),(46,15),'varie'); text(ax,35,20,r'carré $=-1$ ?','varie','s')
box(ax,46,10,40,10,'limite',fill=False,dash=True,label=r'$(x+?)(x-?)$',size='m')
save(fig,'18-117')
