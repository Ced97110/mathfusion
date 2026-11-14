import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(58)
c=(44,30); R=22
line(ax,[(12,30),(80,30)],'fixe')
line(ax,[c,pol(c,R,63.43)],'sujet',1.3)
line(ax,[c,pol(c,R,135)],'resultat',1.3)
line(ax,[c,pol(c,R,-45)],'limite',1.1,dash=True)
arc(ax,c,8,0,63.43,'sujet'); arc(ax,c,11,63.43,135,'autre',1.0)
text(ax,57,36,'63,43°','sujet','s'); text(ax,41,43,'71,57°','autre','s')
text(ax,24,49.5,'somme 135°','resultat','m')
text(ax,62,8,'arctan(−1) = −45°','limite','m')
save(fig,'33-132')
