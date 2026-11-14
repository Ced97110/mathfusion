import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(70)
oy=46; sx=9; sy=4
def axes(cx):
    line(ax,[(cx-20,oy),(cx+20,oy)],'fixe'); line(ax,[(cx,oy-19),(cx,oy+12)],'fixe')
axes(22); axes(66)
text(ax,22,64,'degré 1 : droite','fixe','m'); text(ax,66,64,'degré 2 : parabole','sujet','m')
pts=[(22+x*sx,oy+x*sy) for x in range(-2,3)]
line(ax,[pts[0],pts[-1]],'fixe',lw=1.3)
for p in pts: disc(ax,p[0],p[1],1.2,'fixe')
xs=np.linspace(-2.3,2.3,60)
line(ax,[(66+x*sx,oy+(x*x-4)*sy) for x in xs],'sujet',lw=1.3)
vals=[0,-3,-4,-3,0]
for x,v in zip(range(-2,3),vals):
    px,py=66+x*sx,oy+v*sy
    disc(ax,px,py,1.2,'sujet')
    text(ax,px,py+(3.5 if v==0 else -3.5),f'{v}'.replace('-','−'),'sujet','s')
text(ax,66,20,r'$y=ax^2+bx+c$','sujet','m')
text(ax,44,10,'le terme en $x^2$ courbe','encre','s')
save(fig,'23-069')
