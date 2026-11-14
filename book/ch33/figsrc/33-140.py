import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(56)
cy=24; fx=lambda d: 10+(d+270)/540*70; fy=lambda v: cy+13*v
poly(ax,[(fx(-90),cy-14),(fx(90),cy-14),(fx(90),cy+14),(fx(-90),cy+14)],'sujet')
line(ax,[(10,cy),(80,cy)],'fixe',0.6)
ds=[-270+540*i/200 for i in range(201)]
line(ax,[(fx(d),fy(math.sin(math.radians(d)))) for d in ds],'fixe',1.0)
line(ax,[(fx(d),fy(math.sin(math.radians(d)))) for d in ds if -90<=d<=90],'sujet',1.8)
line(ax,[(10,fy(0.5)),(80,fy(0.5))],'varie',0.9,dash=True)
text(ax,5,fy(0.5),'0,5','varie','s')
disc(ax,fx(30),fy(0.5),1.3,'resultat')
for d in (-210,150): disc(ax,fx(d),fy(0.5),1.3,'autre')
text(ax,fx(0),cy-18,'sinus restreint à [−90°, 90°]','sujet','s')
text(ax,fx(0),47,'une seule fois','resultat','m'); text(ax,fx(150)+2,41,'plusieurs fois','autre','s')
save(fig,'33-140')
