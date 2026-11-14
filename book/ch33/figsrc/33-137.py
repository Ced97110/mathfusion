import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(52)
cy=28; u=9
for cx,pt,ang,cap1,cap2,lab,role in [(22,(1,1),45,'à droite','arctan 1 = 45°','(1 ; 1)','sujet'),(66,(-1,1),135,'à gauche','−45° + 180°','(−1 ; 1)','autre')]:
    c=(cx,cy)
    line(ax,[(cx-14,cy),(cx+14,cy)],'fixe'); line(ax,[(cx,cy-12),(cx,cy+13)],'fixe')
    P=(cx+pt[0]*u,cy+pt[1]*u)
    line(ax,[c,P],role,1.3); disc(ax,P[0],P[1],1.3,role)
    arc(ax,c,6,0,ang,'resultat',1.1)
    q=pol(c,12,22 if ang==45 else 50); text(ax,q[0]+(1 if ang==45 else 2),q[1],f'{ang}°','resultat','s')
    text(ax,P[0]+(2 if pt[0]>0 else -2),P[1]+4,lab,role,'s',ha='left' if pt[0]>0 else 'right')
    text(ax,cx,13,cap1,'encre','s'); text(ax,cx,7,cap2,'resultat','s')
save(fig,'33-137')
