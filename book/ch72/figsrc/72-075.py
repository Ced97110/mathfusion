import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
ox,oy,k=22,35,14
fig,ax=canvas(70)
line(ax,[(4,oy),(82,oy)],'fixe',lw=1.2); text(ax,80,oy+3,'H','fixe','s')
arrow(ax,(ox,oy),(ox,oy+k),'sujet'); text(ax,ox-2,oy+k,r'$u$','sujet','m',ha='right')
arrow(ax,(ox,oy),(ox+3*k,oy),'fixe',lw=1.4); text(ax,ox+3*k-2,oy+4,'v = (3, 0) : reste','fixe','s',ha='right')
arrow(ax,(ox,oy),(ox+k,oy+k),'varie'); arrow(ax,(ox,oy),(ox+k,oy-k),'resultat')
text(ax,ox+k+2,oy+k,'(1, 1)','varie','s',ha='left'); text(ax,ox+k+2,oy-k,'(1, −1) : bouge','resultat','s',ha='left')
save(fig,'72-075')
