import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
u=14; yD=12; xa,xb=24,38
line(ax,[(6,yD),(82,yD)],'fixe',lw=1.8)
text(ax,82,yD-4,r'$D$ : hauteur 0','fixe','s',ha='right')
yp=yD+2*u
line(ax,[(xa,yD),(xa,yp)],'fixe',dash=True)
text(ax,xa+2,yD+u,'hauteur 2','fixe','s',ha='left')
arrow(ax,(xa+1.5,yp),(xb-1.5,yp),'varie',lw=1.3)
disc(ax,xa,yD,1.3,'fixe'); disc(ax,xa,yp,1.3,'varie'); disc(ax,xb,yp,1.3,'resultat')
text(ax,xa,yD-4,'(5, 0) : reste','fixe','s')
text(ax,xa+3,yD+3.4,'glisse de 0','fixe','s',ha='left')
text(ax,xa-3,yp,'(5, 2)','varie','s',ha='right'); text(ax,xb+3,yp,'(6, 2)','resultat','s',ha='left')
text(ax,(xa+xb)/2,yp+4,'glisse de 1','varie','s')
text(ax,62,yp,r'parallèle à $D$','sujet','s',ha='left')
save(fig,'73-015')
