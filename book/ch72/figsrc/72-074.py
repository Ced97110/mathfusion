import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
ox,oy,k=34,35,22
fig,ax=canvas(70)
line(ax,[(6,oy),(82,oy)],'fixe',lw=1.2); text(ax,12,oy+3,'axe H','fixe','s')
arrow(ax,(ox,oy),(ox,oy+k),'sujet'); arrow(ax,(ox,oy),(ox,oy-k),'resultat')
text(ax,ox+3,oy+k-2,r'$u$ = (0, 1)','sujet','s',ha='left')
text(ax,ox+3,oy-k+2,r'$S_u(u)=-u$ = (0, −1)','resultat','s',ha='left')
text(ax,44,5,r'$u - 2u = -u$','encre','m')
save(fig,'72-074')
