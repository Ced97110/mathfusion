import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
ox,oy,k=10,10,9
fig,ax=canvas(52)
arrow(ax,(ox,oy),(ox+k,oy+2*k),'sujet'); arrow(ax,(ox,oy),(ox+3*k,oy+4*k),'autre')
text(ax,ox+k-2,oy+2*k+2,r'$x$ = (1, 2)','sujet','s',ha='right'); text(ax,ox+3*k-2,oy+4*k+3,r'$y$ = (3, 4)','autre','s',ha='right')
box(ax,46,24,38,12,'resultat',label=r'$B(x,y)=11$',size='m')
text(ax,65,16,r'$1\times3+2\times4=11$','resultat','s')
save(fig,'72-079')
