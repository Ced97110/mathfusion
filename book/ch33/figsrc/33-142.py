import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(50)
cy=28; R=11
for cx,cap,cr in [(15,'cosinus seul','encre'),(44,'sinus seul','encre'),(73,'les deux ensemble','resultat')]:
    line(ax,[(cx-13,cy),(cx+13,cy)],'fixe',0.6); line(ax,[(cx,cy-13),(cx,cy+13)],'fixe',0.6)
    arc(ax,(cx,cy),R,0,360,'fixe',0.8)
    text(ax,cx,10,cap,cr,'s')
    if cx!=44: line(ax,[(cx+R*0.5,cy-R),(cx+R*0.5,cy+R)],'varie',1.0,dash=True)
    if cx!=15: line(ax,[(cx-R,cy+R*0.866),(cx+R,cy+R*0.866)],'varie',1.0,dash=True)
def dot(cx,a,t,role,side):
    p=pol((cx,cy),R,a); disc(ax,p[0],p[1],1.3,role)
    text(ax,p[0]+(2.2 if side>0 else -2.2),p[1]+(2.5 if a>0 else -2.5),t,role,'s',ha='left' if side>0 else 'right')
dot(15,60,'60°','sujet',1); dot(15,-60,'−60°','sujet',1)
dot(44,60,'60°','autre',1); dot(44,120,'120°','autre',-1)
dot(73,60,'60°','resultat',1)
save(fig,'33-142')
