import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(62)
u=2.8; x0=26; y0=16
R(ax,x0,y0,10*u,10*u,'sujet'); R(ax,x0+10*u,y0,2*u,10*u,'varie')
R(ax,x0,y0+10*u,10*u,3*u,'varie'); R(ax,x0+10*u,y0+10*u,2*u,3*u,'fixe')
text(ax,x0+14,y0+14,r'$x^2$','sujet','l'); text(ax,x0+10*u+2.8,y0+14,r'$2x$','varie','s')
text(ax,x0+14,y0+10*u+4.2,r'$3x$','varie','m'); text(ax,x0+10*u+2.8,y0+10*u+4.2,'6','fixe','m')
brace(ax,x0,x0+10*u,y0,'sujet',label=r'$x$'); brace(ax,x0+10*u,x0+12*u,y0,'varie',label='2')
text(ax,x0-3,y0+14,r'$x$','sujet','m',ha='right'); text(ax,x0-3,y0+10*u+4.2,'3','varie','m',ha='right')
text(ax,44,y0-12,r'$2x$ et $3x$ ont le côté $x$','varie','s')
save(fig,'18-016')
