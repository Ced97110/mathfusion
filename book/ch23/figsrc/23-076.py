import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(60)
cx=44; oy=26; sx=10; sy=4
line(ax,[(6,oy),(84,oy)],'fixe')
xs=np.linspace(-2.2,2.2,70)
line(ax,[(cx+x*sx,oy+x*x*sy) for x in xs],'fixe',lw=1.0,dash=True)
line(ax,[(cx+x*sx,oy+(x*x+2)*sy) for x in xs],'sujet',lw=1.5)
for x in range(-2,3):
    v=x*x+2
    disc(ax,cx+x*sx,oy+v*sy,1.3,'sujet')
    text(ax,cx+x*sx,oy+v*sy+3.8,str(v),'sujet','s')
arrow(ax,(cx,oy+0.5),(cx,oy+2*sy-1.8),'varie')
text(ax,cx,oy-4,'monter de 2 : c = 2','varie','s')
text(ax,cx,oy-10,r'$D=0-4\times1\times2=-8$','encre','s')
text(ax,cx,oy-16,'aucun point commun avec l’axe','sujet','s')
text(ax,cx+30,oy+8,r'$y=x^2$','fixe','s')
save(fig,'23-076')
