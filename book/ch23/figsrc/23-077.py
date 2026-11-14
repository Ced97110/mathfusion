import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(62)
cx=44; oy=32; sx=11; sy=5
line(ax,[(8,oy),(80,oy)],'fixe')
xs=np.linspace(-1.2,3.2,80)
line(ax,[(cx+(x-1)*sx,oy+((x-1)**2-4)*sy) for x in xs],'sujet',lw=1.5)
line(ax,[(cx,oy-4*sy-3),(cx,oy+14)],'varie',lw=1.3,dash=True)
for v in range(-1,4):
    px=cx+(v-1)*sx
    ax.plot([px,px],[oy-1,oy+1],color=COL['fixe'],lw=0.8,zorder=1.5)
    text(ax,px,oy+3.5 if v!=1 else oy+3.5,str(v).replace('-','−'),'fixe','s') if False else None
line(ax,[(cx-sx,oy-3*sy),(cx+sx,oy-3*sy)],'fixe',lw=0.8,dash=True)
for x in (0,2): disc(ax,cx+(x-1)*sx,oy-3*sy,1.2,'sujet')
for x in (-1,3): disc(ax,cx+(x-1)*sx,oy,1.5,'resultat')
disc(ax,cx,oy-4*sy,1.7,'varie')
text(ax,cx-2*sx-6,oy-4.5,'A','resultat','m'); text(ax,cx+2*sx+6,oy-4.5,'B','resultat','m')
text(ax,cx,oy-4*sy-5,r'$S(1,\ -4)$','varie','s')
text(ax,cx+9,oy+16,r'axe $x=1$','varie','s')
for s in (-1,1):
    arrow(ax,(cx+s*0.8,oy+6),(cx+s*(2*sx-0.8),oy+6),'fixe')
    text(ax,cx+s*sx,oy+9,'2','fixe','s')
text(ax,cx,oy+22,r'$y=(x-1)^2-4$','sujet','m')
save(fig,'23-077')
