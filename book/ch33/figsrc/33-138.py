import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(58)
c=(44,30); R=18
arc(ax,c,R,180,360,'fixe',0.8); arc(ax,c,R,0,180,'sujet',1.8)
line(ax,[(24,30),(64,30)],'fixe',0.6)
x=c[0]-0.5*R
line(ax,[(x,12),(x,48)],'varie',dash=True)
P1=pol(c,R,120); P2=pol(c,R,240)
disc(ax,P1[0],P1[1],1.3,'resultat'); disc(ax,P2[0],P2[1],1.3,'limite')
text(ax,P1[0]-2,P1[1]+1,'120°','resultat','m',ha='right'); text(ax,P2[0]-2,P2[1]-1,'240°','limite','m',ha='right')
text(ax,x,7.5,'cos = −0,5','varie','m')
text(ax,58,46,'arccos : 0° à 180°','sujet','s',ha='left')
text(ax,66,30,'0°','fixe','s',ha='left'); text(ax,22,30,'180°','fixe','s',ha='right')
save(fig,'33-138')
