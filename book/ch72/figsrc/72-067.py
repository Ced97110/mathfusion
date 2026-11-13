import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
ox,oy,k=30,35,16
fig,ax=canvas(70)
line(ax,[(6,oy),(82,oy)],'fixe',lw=1.2); text(ax,12,oy+3,'axe H','fixe','s')
arrow(ax,(ox,oy),(ox,oy+k),'sujet'); text(ax,ox-3,oy+k-2,'u','sujet','m',ha='right')
x=(ox+2*k,oy+k); s=(ox+2*k,oy-k)
disc(ax,*x,1.3,'varie'); disc(ax,*s,1.3,'resultat')
line(ax,[x,s],'fixe',dash=True); disc(ax,x[0],oy,1.0,'fixe')
text(ax,x[0]-3,x[1]+3,'x = (2, 1)','varie','s',ha='right')
text(ax,s[0]-3,s[1]-3,'S(x) = (2, −1)','resultat','s',ha='right')
text(ax,ox+3,oy+k+4,'u = (0, 1)','sujet','s',ha='left')
text(ax,44,6,r'$x - 2u$ : on retire 2 fois $u$','encre','s')
save(fig,'72-067')
