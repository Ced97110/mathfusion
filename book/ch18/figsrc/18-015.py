import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(40)
u=2.5; y0=14
R(ax,12,y0,10*u,3*u,'sujet'); R(ax,12+10*u,y0,3*u,4*u,'autre')
line(ax,[(12,y0+3*u),(12+10*u,y0+3*u),(12+10*u,y0+4*u),(12+10*u+3*u,y0+4*u)],'limite',lw=1.6)
text(ax,8,y0+3.75,'3','sujet','m'); text(ax,12+10*u+3*u+3,y0+5,'4','autre','m')
text(ax,44,36,'bord du haut : 3 puis 4','limite','s')
text(ax,44,6,'pas un rectangle','limite','m')
save(fig,'18-015')
