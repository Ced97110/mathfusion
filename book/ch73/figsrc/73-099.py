import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58); cx,cy,R=18,12,30
P=lambda a,r=R:(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))

def arcarr(ax,c,r,a0,a1,role,lw=1.0):
    n=24; pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw); arrow(ax,pts[-2],pts[-1],role,lw)

line(ax,[(cx-4,cy-4),(cx+38,cy+38)],'sujet',lw=1.3)
line(ax,[P(0),P(90)],'fixe',dash=True,lw=0.7)
arrow(ax,(cx,cy),P(0),'fixe',lw=1.2); arrow(ax,(cx,cy),P(90),'encre',lw=1.4)
disc(ax,*P(45),1.2,'resultat')
arcarr(ax,(cx,cy),11,0,45,'varie'); arcarr(ax,(cx,cy),11,45,90,'varie')
t=P(22.5,17); text(ax,t[0],t[1],r'$\theta/2$','varie','s'); t=P(67.5,17); text(ax,t[0]-1,t[1],r'$\theta/2$','varie','s')
text(ax,50,10,r'$e_1$ : angle 0','fixe','s',ha='left')
text(ax,21,44,r'image de $e_1$ : angle $\theta=90°$','encre','s',ha='left')
text(ax,58,47,r'miroir : angle $\theta/2$','sujet','s',ha='left')
text(ax,43,29,r'$d$ ne bouge pas','resultat','s',ha='left')
save(fig,'73-099')
