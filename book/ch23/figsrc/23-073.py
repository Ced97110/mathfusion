import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(80)
box(ax,2,66,34,10,'sujet',True,r'$x^2-4=0$')
arrow(ax,(37,71),(49,71),'fixe')
box(ax,50,66,36,10,'resultat',True,r'solutions : $-2$ et $2$',size='s')
cx=44; oy=34; sx=11; sy=4.5
line(ax,[(6,oy),(84,oy)],'resultat',lw=1.8); line(ax,[(cx,oy-19),(cx,oy+20)],'fixe')
xs=np.linspace(-3,3,80)
line(ax,[(cx+x*sx,oy+(x*x-4)*sy) for x in xs],'sujet',lw=1.4)
for x in (-2,2):
    disc(ax,cx+x*sx,oy,1.7,'resultat')
    text(ax,cx+x*sx+(-4 if x<0 else 4),oy-4,f'{x}'.replace('-','−'),'resultat','s')
text(ax,76,oy+4,'$y=0$','resultat','s')
text(ax,cx+13,oy+14,r'$y=x^2-4$','sujet','s')
text(ax,44,5,'les solutions sont sur l’axe','resultat','s')
save(fig,'23-073')
