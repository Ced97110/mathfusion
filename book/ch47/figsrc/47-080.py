import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(84)
cs=5.2
text(ax,40,80,'rotations','sujet','s'); text(ax,64,80,'retournements','autre','s')
data=[('carré',4,'8 = 4 × 2'),('triangle',3,'6 = 3 × 2'),('hexagone',6,'12 = 6 × 2')]
for i,(nm,n,eq) in enumerate(data):
    yc=62-i*24
    pts=[(12+7*math.cos(math.pi/2+2*math.pi*k/n+(math.pi/n if n==4 else 0)),yc+7*math.sin(math.pi/2+2*math.pi*k/n+(math.pi/n if n==4 else 0))) for k in range(n)]
    poly(ax,pts,'sujet'); text(ax,12,yc-11,nm,'fixe','s')
    for c in range(n):
        box(ax,26+c*cs,yc+0.6,cs-0.5,cs-0.5,'sujet',r=0.3); box(ax,26+c*cs,yc-5.6,cs-0.5,cs-0.5,'autre',r=0.3)
    text(ax,76,yc,eq,'resultat','m')
save(fig,'47-080')
