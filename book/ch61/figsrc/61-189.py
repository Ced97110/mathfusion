import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(o,R,t): return (o[0]+R*math.cos(math.radians(t)),o[1]+R*math.sin(math.radians(t)))
def draw(o,step,role,dash,lab):
    n=int(round((90 if step==30 else 60)/step))
    for i in range(n+1):
        line(ax,[o,pol(o,34,i*step)],'fixe',lw=0.7)
    for i in range(n):
        arc=[pol(o,34,i*step+step*j/12) for j in range(13)]
        line(ax,arc,role,lw=1.5,dash=dash)
        p=pol(o,22,i*step+step/2); text(ax,p[0],p[1],lab,role,'s')
fig,ax=canvas(60)
draw((6,12),30,'resultat',False,'30°')
draw((49,12),20,'limite',True,'20°')
text(ax,23,53,r'$90°$ en trois','sujet'); text(ax,66,53,r'$60°$ en trois','sujet')
text(ax,23,5,'constructible','resultat'); text(ax,66,5,'impossible','limite')
save(fig,'61-189')
