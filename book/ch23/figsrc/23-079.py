import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(66)
oy=36; sx=8; sy=3.5
xs=np.linspace(-2.4,2.4,60)
for cx,sg,f,cap in [(22,1,r'$y=x^2-4$',r'$S$ : le plus bas, $-4$'),(66,-1,r'$y=4-x^2$',r'$S$ : le plus haut, $4$')]:
    line(ax,[(cx-19,oy),(cx+19,oy)],'fixe')
    line(ax,[(cx+x*sx,oy+sg*(x*x-4)*sy) for x in xs],'sujet',lw=1.4)
    Sy=oy-sg*4*sy
    disc(ax,cx,Sy,1.9,'varie')
    text(ax,cx,60,f,'sujet','m')
    text(ax,cx,Sy-5.5*sg if sg>0 else Sy+5.5,cap,'varie','s')
    # direction arrows on the branches
    for side in (-1,1):
        x0,x1=(1.9,0.7)
        p=(cx+side*x0*sx, oy+sg*(x0*x0-4)*sy); q=(cx+side*x1*sx, oy+sg*(x1*x1-4)*sy)
        arrow(ax,p if side<0 else q, q if side<0 else p,'autre') if False else None
text(ax,44,6,'la courbe change de sens en S','encre','s')
save(fig,'23-079')
