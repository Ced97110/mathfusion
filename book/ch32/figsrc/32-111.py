import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(66)
cx,cy,R=36,34,22
disc(ax,cx,cy,R,'fixe',fill=False,lw=1.0)
ya=cy+0.5*R; yb=cy-R
line(ax,[(4,ya),(84,ya)],'sujet',lw=1.1); line(ax,[(4,yb),(84,yb)],'autre',lw=1.1)
dx=R*math.sqrt(0.75)
disc(ax,cx+dx,ya,1.5,'resultat'); disc(ax,cx-dx,ya,1.5,'resultat'); disc(ax,cx,yb,1.5,'resultat')
text(ax,cx+dx+5,ya+3.5,'30°','resultat','s'); text(ax,cx-dx-5,ya+3.5,'150°','resultat','s'); text(ax,cx,yb-3.5,'−90°','resultat','s')
text(ax,76,ya+3.5,'y = 0,5','sujet','s'); text(ax,76,yb+3.5,'y = −1','autre','s')
text(ax,cx,cy,'2 + 1 = 3','resultat','m')
save(fig,'32-111')
