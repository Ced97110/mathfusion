import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(58)
cx,cy=30,18; c=(cx,cy); u=16
line(ax,[(6,cy),(80,cy)],'fixe'); line(ax,[(cx,6),(cx,46)],'fixe')
P1=(cx+u,cy+u); P2=(cx-u,cy+u)
line(ax,[c,P1],'sujet',1.3); line(ax,[c,P2],'autre',1.3)
disc(ax,P1[0],P1[1],1.3,'sujet'); disc(ax,P2[0],P2[1],1.3,'autre')
disc(ax,cx+u,cy,1.3,'fixe'); text(ax,cx+u,cy-4,'1','fixe','s')
arc(ax,c,9,0,45,'varie',1.1,True); arc(ax,c,17,0,135,'varie',1.1,True)
q=pol(c,12.5,20); text(ax,q[0],q[1],'45°','sujet','s')
q=pol(c,12.5,115); text(ax,q[0],q[1],'135°','autre','s')
text(ax,P1[0]+3,P1[1]+2,'1 + i','sujet','s',ha='left'); text(ax,P2[0]-3,P2[1]+2,'−1 + i','autre','s',ha='right')
text(ax,44,52,'× (a + bi) : on tourne','encre','m')
save(fig,'33-143')
