import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
import math
ys=[62,36,10]
for y in ys: box(ax,3,y,46,20,'fixe')
cx,cy=14,72
for k in range(12):
    t=math.radians(90-30*k); disc(ax,cx+6*math.cos(t),cy+6*math.sin(t),0.9,'fixe')
text(ax,36,72,'horloge','fixe','s')
poly(ax,[(8,40),(20,40),(20,52),(8,52)],'fixe',fill=False)
text(ax,36,46,'carré','fixe','s')
for (x,y) in [(14,28),(8,15),(20,15)]: disc(ax,x,y,1.6,'fixe')
line(ax,[(14,28),(8,15),(20,15),(14,28)],'fixe',lw=0.6)
text(ax,36,20,'3 objets','fixe','s')
box(ax,60,32,25,22,'sujet',label='G',size='xl')
for y in (72,46,20): arrow(ax,(50,y),(59,43),'sujet')
text(ax,72.5,26,'un groupe','sujet','s') if False else None
text(ax,72.5,25,'quelconque','sujet','s')
save(fig,'47-044')
