import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(52)
u=2.5; y0=18
R(ax,6,y0,10*u,3*u,'sujet'); R(ax,56,y0,3*u,3*u,'autre')
text(ax,6+12.5,y0+3.75,'aire 30','sujet','s'); text(ax,56+3.75,y0+3.75,'9','autre','m')
line(ax,[(2,y0+3*u),(86,y0+3*u)],'fixe',dash=True)
for xx in (4,54):
    arrow(ax,(xx,y0),(xx,y0+3*u),'varie',both=True)
text(ax,6+12.5,y0+3*u+3,'hauteur 3','varie','s'); text(ax,56+3.75,y0+3*u+3,'3','varie','m')
text(ax,44,8,'3 est une hauteur, pas une aire','encre','s')
save(fig,'18-014')
