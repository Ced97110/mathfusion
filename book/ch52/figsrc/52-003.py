import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
cx,cy,R=24,36,12
fig,ax=canvas(62)
disc(ax,cx,cy,R,'fixe')
P=lambda h,r: (cx+r*math.sin(math.radians(30*h)), cy+r*math.cos(math.radians(30*h)))
for h in range(12):
    x,y=P(h,R); ax.plot([x,P(h,R-1.8)[0]],[y,P(h,R-1.8)[1]],color=COL['fixe'],lw=0.8,zorder=3)
for h,lab in [(0,'12'),(3,'3'),(6,'6')]:
    text(ax,*P(h,R-4.6),lab,'fixe','s')
for h,r in [(9,'sujet'),(2,'resultat')]:
    x,y=P(h,R); disc(ax,x,y,1.6,r)
text(ax,*P(9,R+3.8),'9','sujet','m',weight='bold'); text(ax,*P(2,R+3.8),'2','resultat','m',weight='bold')
def arc(r,h0,h1,role,dash):
    n=60; pts=[P(h0+(h1-h0)*i/n,r) for i in range(n+1)]
    line(ax,pts[:-1],role,dash=dash); arrow(ax,pts[-2],pts[-1],role)
arc(R+8,9,14,'varie',False)
arc(R+12,9,26,'autre',True)
text(ax,65,46,'9 + 5 = 14','varie','m'); text(ax,65,40,'reste 2','resultat','m')
text(ax,65,30,'9 + 17 = 26','autre','m'); text(ax,65,24,'reste 2','resultat','m')
text(ax,65,12,'ℤ/12ℤ : 12 restes','sujet','m')
save(fig,'52-003')
