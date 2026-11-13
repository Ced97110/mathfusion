import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(70)
oy=40; sx=5.2; sy=2.6
text(ax,44,66,'même forme, hauteur change','encre','s')
line(ax,[(2,oy),(86,oy)],'fixe')
xs=np.linspace(-2.4,2.4,60)
specs=[(15,-4,'sujet',r'$x^2-4$','sommet −4\n2 points sur l’axe',(-2,2)),
       (44,0,'resultat',r'$x^2$','sommet 0\n1 point sur l’axe',(0,)),
       (73,2,'autre',r'$x^2+2$','sommet 2\n0 point sur l’axe',())]
for cx,c,r,f,cap,roots in specs:
    line(ax,[(cx+x*sx,oy+(x*x+c)*sy) for x in xs],r,lw=1.4)
    for x in roots: disc(ax,cx+x*sx,oy,1.5,r)
    text(ax,cx,24,f,r,'m')
    text(ax,cx,12,cap,r,'s')
save(fig,'23-074')
