import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
u=10
x0,y0=24,20
box(ax,x0,y0,4*u,3*u,'fixe',fill=False,lw=1.0)
poly(ax,[(x0,y0),(x0+4*u,y0),(x0+4*u,y0+3*u)],'sujet')
line(ax,[(x0,y0),(x0+4*u,y0+3*u)],'sujet',lw=2.2)
line(ax,[(x0+4*u-2.4,y0),(x0+4*u-2.4,y0+2.4),(x0+4*u,y0+2.4)],'encre',lw=0.7)
text(ax,x0+2*u,15,'4 m','fixe','m'); text(ax,x0-5,y0+1.5*u,'3 m','fixe','m')
text(ax,x0+12,y0+3*u-4,'hypoténuse : câble 5 m','resultat','m')
text(ax,76,y0+7,'angle droit','encre','s')
arrow(ax,(70,y0+4.5),(x0+4*u+0.8,y0+1.5),'varie')
text(ax,44,6,'$3^2+4^2=25$','resultat','m')
save(fig,'22-134')
