import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(52)
r=7.5; cy=28
for cx,d,role,t1,t2 in ((13,0.5*r*2,'fixe','coupe : 2 points','à 0,5 du centre'),(41,r,'sujet','touche : 1 point','à 1 du centre'),(66,2*r,'fixe','aucun point','à 2 du centre')):
    if cx==13: d=r/2
    disc(ax,cx,cy,r,'fixe',fill=False)
    line(ax,[(cx+d,cy-12),(cx+d,cy+12)],role,lw=1.8 if role=='sujet' else 0.9)
    text(ax,cx+d/2+1,11,t1,role,'s'); text(ax,cx+d/2+1,6,t2,'fixe','s')
h=math.sqrt(r*r-(r/2)**2)
for s in (1,-1): disc(ax,13+r/2,cy+s*h,0.9,'limite')
disc(ax,41+r,cy,1.0,'resultat')
text(ax,41+r,45,'tangente','sujet','s')
save(fig,'25-047')
