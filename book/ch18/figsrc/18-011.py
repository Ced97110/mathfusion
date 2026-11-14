import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(46)
u=3; x0=24; y0=22
R(ax,x0,y0,10*u,3*u,'sujet'); R(ax,x0+10*u,y0,3*u,3*u,'varie')
text(ax,x0+15,y0+4.5,'30','sujet','m'); text(ax,x0+10*u+4.5,y0+4.5,'9','varie','m')
text(ax,x0-3,y0+4.5,'3','fixe','m',ha='right')
brace(ax,x0,x0+10*u,y0,'sujet',label=r'$2x$ = 10')
brace(ax,x0+10*u,x0+13*u,y0,'varie',label='3')
brace(ax,x0,x0+13*u,y0-9,'resultat',label=r'$2x+3$ = 13')
text(ax,44,43,r'$6x+9=3(2x+3)$','encre','m')
save(fig,'18-011')
