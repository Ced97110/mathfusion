import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(62)
cx,cy,u=44,30,13; c=(cx,cy)
line(ax,[(12,cy),(78,cy)],'fixe'); line(ax,[(cx,6),(cx,57)],'fixe')
P=(cx-u,cy+u); Q=(cx+u,cy-u)
line(ax,[c,P],'sujet',1.3); line(ax,[c,Q],'autre',1.0,dash=True)
disc(ax,P[0],P[1],1.3,'sujet'); disc(ax,Q[0],Q[1],1.3,'autre')
arc(ax,c,7,0,135,'resultat'); arc(ax,c,7,0,-45,'autre')
arc(ax,c,25,-45,135,'varie',1.1,True)
text(ax,39.5,40,'135°','resultat','s'); text(ax,55.5,26,'−45°','autre','s')
text(ax,64.5,50.5,'+ 180°','varie','m')
text(ax,29,39.5,'(−1 ; 1)','sujet','s',ha='right'); text(ax,59,13.5,'(1 ; −1)','autre','s',ha='left')
save(fig,'33-133')
