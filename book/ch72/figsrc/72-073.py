import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
x0,y0,k=30,38,9
fig,ax=canvas(76)
box(ax,6,y0-1.5,76,3,'sujet'); text(ax,10,y0+4,'H','sujet','m',weight='bold')
line(ax,[(x0,y0-3*k-3),(x0,y0+3*k+3)],'fixe',dash=True)
for z,r,l in ((3,'varie','(1, 2, 3)'),(0,'sujet','M = (1, 2, 0)'),(-3,'resultat','(1, 2, −3)')):
    disc(ax,x0,y0+z*k,1.5,r); text(ax,x0+4,y0+z*k+(4 if z==0 else 0),l,r,'s',ha='left')
arrow(ax,(x0-2,y0+3*k-1.5),(x0-2,y0+1.5),'varie',curve=0.4); text(ax,x0-12,y0+1.5*k,'1re fois','varie','s')
arrow(ax,(x0-2,y0-1.5),(x0-2,y0-3*k+1.5),'varie',curve=0.4); text(ax,x0-12,y0-1.5*k,'2e fois','varie','s')
text(ax,66,y0+1.5*k,'retirer (0, 0, 3)','varie','s'); 
save(fig,'72-073')
