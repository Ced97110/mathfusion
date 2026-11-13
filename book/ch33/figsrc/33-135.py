import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(58)
s=6.5; A=(8,14); C=(A[0]+8*s*math.cos(math.radians(30)),A[1]+8*s*math.sin(math.radians(30)))
B1=(A[0]+3.93*s,14); B2=(A[0]+9.93*s,14)
line(ax,[(8,14),(82,14)],'fixe')
line(ax,[A,C],'fixe',1.2)
line(ax,[C,B1],'sujet',1.3); line(ax,[C,B2],'autre',1.3)
arc(ax,A,10,0,30,'fixe')
arc(ax,B1,5,53.13,180,'sujet'); arc(ax,B2,5,126.87,180,'autre')
text(ax,22,17.8,'30°','fixe','s')
text(ax,29,30,'8','fixe','m'); text(ax,39,28,'5','sujet','m'); text(ax,66.5,28,'5','autre','m')
text(ax,B1[0],8.5,'126,87°','sujet','s'); text(ax,B2[0],8.5,'53,13°','autre','s')
text(ax,66,50,'sin B = 0,8','encre','m')
save(fig,'33-135')
