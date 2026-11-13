import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(68)
cx,cy,R=44,34,20
disc(ax,cx,cy,R,'fixe',fill=False,lw=1.0)
x1=cx-R; x2=cx+0.5*R
line(ax,[(x1,8),(x1,60)],'sujet',lw=1.1); line(ax,[(x2,8),(x2,60)],'autre',lw=1.1)
disc(ax,x1,cy,1.5,'resultat')
h=R*math.sqrt(0.75)
disc(ax,x2,cy+h,1.5,'resultat'); disc(ax,x2,cy-h,1.5,'resultat')
text(ax,x1,64,'x = −1','sujet','s'); text(ax,x2,64,'x = 0,5','autre','s')
text(ax,13,cy,'1 seul point','sujet','s'); text(ax,77,cy,'2 points','autre','s')
save(fig,'32-108')
