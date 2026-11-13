import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(66)
cx=44; oy=30; sx=11; sy=4.5
line(ax,[(6,oy),(82,oy)],'fixe'); line(ax,[(cx,oy-19),(cx,oy+25)],'fixe')
for v in range(-3,4): ax.plot([cx+v*sx]*2,[oy-1,oy+1],color=COL['fixe'],lw=0.8,zorder=1.5)
xs=np.linspace(-3,3,80)
line(ax,[(cx+x*sx,oy+(x*x-4)*sy) for x in xs],'sujet',lw=1.4)
line(ax,[(cx,oy-4*sy),(cx,oy)],'varie',dash=True)
for x,n,r in [(-2,'A','resultat'),(2,'B','resultat')]:
    disc(ax,cx+x*sx,oy,1.6,r)
disc(ax,cx,oy-4*sy,1.6,'varie')
text(ax,cx-2*sx-8,oy-4.5,r'$A(-2,\ 0)$','resultat','s')
text(ax,cx+2*sx+8,oy-4.5,r'$B(2,\ 0)$','resultat','s')
text(ax,cx,oy-4*sy-4.5,r'$S(0,\ -4)$','varie','s')
for s in (-1,1):
    arrow(ax,(cx+s*0.8,oy+4),(cx+s*(2*sx-0.8),oy+4),'fixe')
    text(ax,cx+s*sx,oy+7,'2','fixe','s')
text(ax,70,oy+22,r'$y=x^2-4$','sujet','m')
save(fig,'23-070')
