import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(66)
cx=44; oy=34; sx=11; sy=4.5
line(ax,[(6,oy),(82,oy)],'fixe'); line(ax,[(cx,oy-19),(cx,oy+22)],'fixe')
xs=np.linspace(-3,3,80)
line(ax,[(cx+x*sx,oy+(x*x-4)*sy) for x in xs],'fixe',lw=1.3)
line(ax,[(cx,oy),(cx-2*sx,oy)],'sujet',lw=2.2); line(ax,[(cx,oy),(cx+2*sx,oy)],'sujet',lw=2.2)
for x in (-2,2): disc(ax,cx+x*sx,oy,1.7,'resultat')
text(ax,cx-2*sx-1,oy+4.5,'A','resultat','m'); text(ax,cx+2*sx+1,oy+4.5,'B','resultat','m')
text(ax,cx-sx,oy+5.5,'abscisse −2','sujet','s'); text(ax,cx+sx,oy+5.5,'abscisse 2','sujet','s')
text(ax,cx-sx,oy-4,'−2','sujet','s') if False else None
text(ax,cx,oy-7,'ordonnée de A et B : 0','autre','s')
text(ax,cx,6,r'$A(-2,\ 0)$ : abscisse = 1er nombre','encre','s')
save(fig,'23-110')
