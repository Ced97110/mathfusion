import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
u=3.6; xL=7; xR=54; y0=14
sq=lambda x,y,w,h:[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
poly(ax,sq(xL,y0,5*u,3*u),'sujet'); text(ax,xL+2.5*u,y0+1.5*u,'15','sujet','m')
poly(ax,sq(xL,y0+3*u,3*u,2*u),'varie'); text(ax,xL+1.5*u,y0+4*u,'6','varie','m')
poly(ax,sq(xL+3*u,y0+3*u,2*u,2*u),'fixe',fill=False); text(ax,xL+4*u,y0+4*u,'4','fixe','s')
text(ax,xL+2.5*u,y0-3.5,'5','encre','s'); text(ax,xL-3.5,y0+1.5*u,'3','sujet','s'); text(ax,xL-3.5,y0+4*u,'2','varie','s')
poly(ax,sq(xR,y0,5*u,3*u),'sujet'); text(ax,xR+2.5*u,y0+1.5*u,'15','sujet','m')
poly(ax,sq(xR+5*u,y0,2*u,3*u),'varie'); text(ax,xR+6*u,y0+1.5*u,'6','varie','m')
text(ax,xR+3.5*u,y0-3.5,'7','encre','s'); text(ax,xR+7*u+3.5,y0+1.5*u,'3','sujet','s')
arrow(ax,(xL+1.5*u,y0+5*u+1.5),(xR+6*u,y0+3*u+2.5),'varie',curve=-0.25)
text(ax,46,47,'on déplace la bande','varie','s')
save(fig,'15-108')
