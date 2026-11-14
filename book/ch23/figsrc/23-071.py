import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(64)
cx=52; oy=48; sx=14; sy=7
for v in (0,-3,-4):
    line(ax,[(18,oy+v*sy),(84,oy+v*sy)],'fixe',lw=0.6,dash=True)
    text(ax,10,oy+v*sy,f'{v}'.replace('-','−'),'fixe','s')
xs=np.linspace(-2.2,2.2,80)
line(ax,[(cx+x*sx,oy+(x*x-4)*sy) for x in xs],'fixe',lw=1.4)
for x in (-2,-1,1,2): disc(ax,cx+x*sx,oy+(x*x-4)*sy,1.4,'fixe')
disc(ax,cx,oy-4*sy,2.2,'sujet')
text(ax,cx,oy-4*sy-5,'sommet : le point le plus bas','sujet','s')
text(ax,cx,oy+9,'un seul point à −4','sujet','s')
arrow(ax,(cx,oy+6),(cx,oy-4*sy+3.5),'sujet')
save(fig,'23-071')
