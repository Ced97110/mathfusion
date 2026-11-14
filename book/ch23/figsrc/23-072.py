import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(92)
cs=[(17,'S','sujet','nomme\nle point'),(44,'0','varie','position\nhorizontale'),(71,'−4','autre','hauteur')]
for cx,l,r,c in cs:
    box(ax,cx-10,76,20,10,r,True,l,size='l')
    text(ax,cx,68,c,r,'s')
ox=50; oy=36; sx=10; sy=6
line(ax,[(8,oy),(84,oy)],'fixe'); line(ax,[(20,oy-28),(20,oy+14)],'fixe')
xs=np.linspace(-2.7,2.7,80)
line(ax,[(ox+x*sx,oy+(x*x-4)*sy) for x in xs],'fixe',lw=1.3)
Sx,Sy=ox,oy-4*sy
line(ax,[(Sx,Sy),(Sx,oy)],'varie',dash=True); line(ax,[(Sx,Sy),(20,Sy)],'autre',dash=True)
disc(ax,Sx,Sy,1.8,'sujet')
text(ax,Sx+6,Sy-3,'S','sujet','m')
text(ax,Sx,oy+4,'0','varie','s'); text(ax,14,Sy,'−4','autre','s')
save(fig,'23-072')
