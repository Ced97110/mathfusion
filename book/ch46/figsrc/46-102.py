import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(75)
def ring(cx,labels,role,title):
    cy=40
    for k in range(4):
        p=cp(cx,cy,11,4,k); disc(ax,p[0],p[1],4,role,label=labels[k],size='s')
    for k in range(4):
        p,q=sh(cp(cx,cy,11,4,k),cp(cx,cy,11,4,k+1),5.2); arrow(ax,p,q,'varie',lw=0.8,curve=-0.25)
    text(ax,cx,66,title,role,'s')
ring(20,['0','1','2','3'],'sujet','horloge à 4 heures')
ring(68,['0°','90°','180°','270°'],'autre','rotations du carré')
arrow(ax,(36,40),(52,40),'resultat',both=True)
text(ax,44,46,'même','resultat','s'); text(ax,44,34,'structure','resultat','s')
text(ax,20,14,'engendré par 1','sujet','s'); text(ax,68,14,'par le quart de tour','autre','s')
text(ax,44,5,'les deux : cyclique d’ordre 4','encre','s')
save(fig,'46-102')
