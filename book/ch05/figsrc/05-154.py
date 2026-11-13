import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(58)
r=18; c1,c2,cy=31,57,30
th=math.acos((c2-c1)/2/r)
lens=[(c1+r*math.cos(t),cy+r*math.sin(t)) for t in [-th+2*th*i/30 for i in range(31)]]
lens+=[(c2+r*math.cos(t),cy+r*math.sin(t)) for t in [math.pi-th+2*th*i/30 for i in range(31)]]
poly(ax,lens,'resultat')
disc(ax,c1,cy,r,'sujet',fill=False,lw=1.1); disc(ax,c2,cy,r,'autre',fill=False,lw=1.1)
text(ax,c1,cy+r+3.5,'diviseurs de 8','sujet','m'); text(ax,c2,cy+r+3.5,'diviseurs de 15','autre','m')
text(ax,24,cy,'2   4   8','sujet','m'); text(ax,64,cy,'3   5   15','autre','m')
text(ax,(c1+c2)/2,cy,'1','resultat','l',weight='bold')
text(ax,44,5,'seul diviseur commun : 1','resultat','m')
save(fig,'05-154')
