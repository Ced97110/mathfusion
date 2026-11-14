import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(62)
cx,cy,R=28,30,24
disc(ax,cx,cy,R,'fixe',fill=False)
line(ax,[(cx-R-2,cy),(cx+R+2,cy)],'fixe',lw=0.5); line(ax,[(cx,cy-R-2),(cx,cy+R+2)],'fixe',lw=0.5)
px,py=cx+R*0.5,cy+R*math.sqrt(3)/2
line(ax,[(cx,cy),(px,py)],'sujet',lw=1.2)
line(ax,[(cx,cy),(px,cy)],'varie',lw=1.6)
line(ax,[(px,cy),(px,py)],'resultat',lw=1.6)
disc(ax,px,py,2,'sujet')
text(ax,cx+13,cy-3.5,'cos 60° = 0,5','varie','s')
text(ax,px+12,cy+(py-cy)/2+2,'sin 60° ≈ 0,866','resultat','s',ha='left')
line(ax,[(px,cy+(py-cy)/2+2),(px+11.5,cy+(py-cy)/2+2)],'resultat',lw=0.5)
text(ax,cx-1.5,cy+12,'1','sujet','m')
text(ax,cx+4,cy+3,'60°','varie','s',ha='left')
text(ax,px+4,py+4,r'$0{,}5+0{,}866\,i$','sujet','s',ha='left')
save(fig,'48-148')
