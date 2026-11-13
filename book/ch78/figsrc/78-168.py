import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
cx,cy,R=18,48,13
disc(ax,cx,cy,R,'fixe',fill=False)
q=(cx+2*R,cy)
line(ax,[(cx-R-2,cy),(q[0]+4,cy)],'fixe',lw=0.5)
for k in range(6):
    a=math.radians(60*k); p=(cx+R*math.cos(a),cy+R*math.sin(a))
    if k in (1,5):
        line(ax,[q,p],'sujet',lw=1.2); disc(ax,p[0],p[1],1.4,'sujet')
    else: disc(ax,p[0],p[1],1.4,'fixe')
disc(ax,q[0],q[1],1.3,'encre')
text(ax,q[0]+3.5,cy+2.5,r'$q$','encre','m')
text(ax,q[0]-6,cy+9.5,r'$\sqrt{3}$','sujet','s')
text(ax,q[0]-6,cy-9.5,r'$\sqrt{3}$','sujet','s')
disc(ax,60,60,1.4,'sujet'); text(ax,63,60,'racine primitive','sujet','s',ha='left')
disc(ax,60,52,1.4,'fixe'); text(ax,63,52,'autre racine','fixe','s',ha='left')
box(ax,8,8,72,12,'resultat',label=r'$\sqrt{3}\times\sqrt{3} = 3 = \Phi_6(2)$')
arrow(ax,(44,28),(44,21),'varie')
save(fig,'78-168')
