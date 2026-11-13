import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(56)
oy=28
for ox,ang,cap in [(4,0,'même sens'),(31,90,'perpendiculaires'),(66,180,'sens opposés')]:
    a=(ox,oy)
    line(ax,[a,(ox+17,oy)],'sujet',2.2); arrow(ax,(ox+15,oy),(ox+17.5,oy),'sujet',1.2)
    v=pol(a,12,ang); line(ax,[a,v],'autre',1.1)
    arrow(ax,pol(a,10,ang),pol(a,12.5,ang),'autre',1.1)
    if ang: arc(ax,a,5,0,ang,'resultat',1.1)
    text(ax,ox+(8 if ang<180 else 2),18,f'{ang}°','resultat','m'); text(ax,ox+(8 if ang<180 else 2),12,cap,'encre','s')
text(ax,44,48,'arccosinus : de 0° à 180°','encre','m')
save(fig,'33-139')
