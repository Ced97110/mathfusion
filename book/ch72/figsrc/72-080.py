import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
ox,oy,k=10,8,14
fig,ax=canvas(52)
arrow(ax,(ox,oy),(ox+2*k,oy+k),'sujet'); text(ax,ox+2*k-2,oy+k+4,r'$x$ = (2, 1)','sujet','s',ha='right')
text(ax,66,46,r'$B(x,x)$','encre','m')
box(ax,46,26,38,14,'sujet',label='habituelle : 5'); text(ax,65,21,r'$2\times2+1\times1$','sujet','s')
box(ax,46,5,38,14,'autre'); text(ax,65,13,'seconde : 3','autre','m'); text(ax,65,8,r'$2\times2-1\times1$','autre','s')
save(fig,'72-080')
