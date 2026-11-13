import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plus(ax,x,y,s=1.6):
    line(ax,[(x-s,y),(x+s,y)],'encre',1.0); line(ax,[(x,y-s),(x,y+s)],'encre',1.0)
def times(ax,x,y,s=1.3):
    line(ax,[(x-s,y-s),(x+s,y+s)],'encre',1.0); line(ax,[(x-s,y+s),(x+s,y-s)],'encre',1.0)
def eq(ax,x,y,s=1.6):
    line(ax,[(x-s,y+0.8),(x+s,y+0.8)],'encre',1.0); line(ax,[(x-s,y-0.8),(x+s,y-0.8)],'encre',1.0)
def mat(ax,x,y,v,roles,cw=7,ch=6,size='m'):
    for r in range(2):
        for c in range(2):
            box(ax,x+c*cw,y+(1-r)*ch,cw,ch,roles[r][c],label=v[r][c],size=size)

fig,ax=canvas(84)
text(ax,44,78,'$u=1+\\sqrt{2}+\\sqrt{3}$','encre','m')
box(ax,2,52,34,12,'fixe',label='$L$ : contient $u$')
box(ax,2,32,34,12,'sujet',label='$E$ : $a+b\\sqrt{2}$')
box(ax,2,12,34,12,'autre',label='$K$ : rationnels')
line(ax,[(19,52),(19,44)],'fixe'); line(ax,[(19,32),(19,24)],'fixe')
box(ax,50,34,36,12,'sujet',label='$N_{L/E}(u)=2\\sqrt{2}$')
box(ax,50,12,36,12,'autre',label='$N_{L/K}(u)=-8$')
arrow(ax,(36,58),(68,46),'sujet'); arrow(ax,(36,56),(60,24),'autre',curve=0.0)
save(fig,'77-054')
