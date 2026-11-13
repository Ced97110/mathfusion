import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(66)
box(ax,28,50,32,10,'fixe',label='aire 24',weight='bold')
u=3
R(ax,5,8,6*u,4*u,'sujet'); text(ax,5+9,14,r'$4\times 6$','sujet','m')
R(ax,50,8,8*u,3*u,'autre'); text(ax,50+12,12.5,r'$3\times 8$','autre','m')
arrow(ax,(40,49),(20,28),'fixe'); arrow(ax,(48,49),(62,28),'fixe')
text(ax,44,34,'?','limite','xl')
text(ax,44,3.5,'même aire, côtés différents','limite','s')
save(fig,'18-003')
