import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(58)
sx,sy,y0=5.6,2.4,24
def panel(cx,fn,role,title,delta,roots,cnt):
    line(ax,[(cx-20,y0),(cx+20,y0)],'fixe',lw=0.6)
    u=np.linspace(-3.6,1.6,200); ax.plot(cx+u*sx,y0+fn(u)*sy,color=COL[role],lw=1.2,zorder=3)
    text(ax,cx,52,title,role,'s'); text(ax,cx,46.5,delta,role,'m')
    for r in roots:
        disc(ax,cx+r*sx,y0,1.3,'resultat'); text(ax,cx+r*sx,y0-3.8,f'{r}'.replace('-','−'),'resultat','s')
    text(ax,cx,5,cnt,'resultat','m')
panel(23,lambda u:u*u+2*u+1,'sujet','u² + 2u + 1','Δ = 0',[-1],'1 racine')
panel(65,lambda u:u*u+2*u-3,'autre','u² + 2u − 3','Δ = 16',[-3,1],'2 racines')
save(fig,'32-107')
