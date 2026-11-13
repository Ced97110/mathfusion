import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
ox,oy,k=18,28,18
fig,ax=canvas(62)
line(ax,[(4,oy),(40,oy)]); line(ax,[(ox,8),(ox,52)])
arrow(ax,(ox,oy),(ox+k,oy+k),'sujet'); arrow(ax,(ox,oy),(ox+k,oy),'varie')
text(ax,ox+k-2,oy+k+4,'u = (1, 1)','sujet','s'); text(ax,ox+k+1,oy-4,'x = (1, 0)','varie','s',ha='center')
box(ax,46,38,38,10,'fixe',label=r'$B(x,u)=1$')
box(ax,46,24,38,10,'sujet',label=r'$B(u,u)=1-1=0$')
box(ax,46,8,38,12,'limite',label=r'$1\,/\,0$ : impossible')
arrow(ax,(65,23),(65,21),'limite')
save(fig,'72-072')
