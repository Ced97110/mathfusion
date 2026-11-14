import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
u=26
x0,y0=8,15
poly(ax,[(x0,y0),(x0+u,y0),(x0+u,y0+u)],'sujet')
box(ax,x0,y0,u,u,'fixe',fill=False,lw=0.9)
line(ax,[(x0,y0),(x0+u,y0+u)],'sujet',lw=2.0)
line(ax,[(x0+u-2.4,y0),(x0+u-2.4,y0+2.4),(x0+u,y0+2.4)],'encre',lw=0.7)
text(ax,x0+u/2,y0-3,'1','fixe','s'); text(ax,x0+u+3,y0+u/2,'1','fixe','s')
text(ax,x0+u/2-3,y0+u/2+4,'$d$','sujet','m')
text(ax,63,46,'$d^2=1^2+1^2$','sujet','m')
text(ax,63,30,'$d^2=2$','sujet','m')
text(ax,63,14,'$d=\\sqrt{2}$','resultat','m')
arrow(ax,(63,42),(63,34),'varie'); arrow(ax,(63,26),(63,18),'varie')
save(fig,'22-137')
