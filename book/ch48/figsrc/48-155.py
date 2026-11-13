import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
cx,cy,R=30,36,19
disc(ax,cx,cy,R,'fixe',fill=False)
def arc(a0,a1,r,role):
    pts=[(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a))) for a in range(a0,a1+1,4)]
    line(ax,pts,role,lw=1.3)
arc(4,116,23,'sujet'); arc(124,236,27,'varie')
for d,r in [(120,'sujet'),(240,'varie'),(0,'resultat')]:
    a=math.radians(d); disc(ax,cx+R*math.cos(a),cy+R*math.sin(a),2.2,r)
text(ax,cx,cy+9,r'$\varphi(\alpha)$ : 120°','sujet','s')
text(ax,cx,cy-9,r'$\varphi(\beta)$ : 240°','varie','s')
text(ax,cx+10,cy,'1','resultat','m')
box(ax,60,44,26,16,'fixe'); text(ax,73,52,'120° + 240°\n= 360° : un tour','encre','s')
arrow(ax,(73,44),(73,29),'varie')
box(ax,60,14,26,15,'resultat'); text(ax,73,21.5,r'$\varphi(\alpha)\varphi(\beta)$'+'\n'+r'$=1=\varphi(2\pi)$','resultat','s')
save(fig,'48-155')
