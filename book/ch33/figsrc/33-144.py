import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(52)
u=16; O=(14,8)
poly(ax,[O,(O[0]+2*u,O[1]),(O[0]+2*u,O[1]+2*u),(O[0],O[1]+2*u)],'fixe',fill=False)
R1=(O[0]+2*u,O[1]+u); R2=(O[0]+2*u,O[1]+2*u)
line(ax,[O,R1],'sujet',1.4); line(ax,[O,R2],'resultat',1.4)
disc(ax,R1[0],R1[1],1.2,'sujet')
arc(ax,O,12,0,26.57,'sujet',1.2); arc(ax,O,17,26.57,45,'autre',1.4)
text(ax,R1[0]+4,R1[1]-6,'26,57°','sujet','m',ha='left')
text(ax,R1[0]+4,R1[1]+6,'18,43°','autre','m',ha='left')
text(ax,R2[0]+4,R2[1],'45°','resultat','l',ha='left')
text(ax,R1[0]-3,R1[1]+1.8,'(2 ; 1)','sujet','s',ha='right')
save(fig,'33-144')
