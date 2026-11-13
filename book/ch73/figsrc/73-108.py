import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arcarr(ax,c,r,a0,a1,role,lw=1.0):
    n=24; pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw); arrow(ax,pts[-2],pts[-1],role,lw)

fig,ax=canvas(58); s=14; o=(10,14)
pl=lambda x,y:(o[0]+s*x,o[1]+s*y)
line(ax,[pl(-0.3,0),pl(2.6,0)],'fixe',lw=0.5); line(ax,[pl(0,-0.3),pl(0,1.6)],'fixe',lw=0.5)
arrow(ax,o,pl(1,0),'fixe',lw=1.2); text(ax,pl(0.5,0)[0],o[1]-4,r'$y$','fixe','s')
arcarr(ax,o,s,0,90,'sujet',lw=1.3); text(ax,o[0]+s*0.85,o[1]+s*0.85,r'$A$','sujet','m')
arrow(ax,pl(0,1),pl(2,1),'varie',lw=1.3); text(ax,pl(1,1)[0]+2,pl(1,1)[1]+4.5,r'$x$','varie','s')
disc(ax,*pl(2,1),1.3,'resultat'); text(ax,pl(2,1)[0]+2,pl(2,1)[1]-4.5,'(2 ; 1)','resultat','s',ha='left')
text(ax,44,52,r'(A, x)(B, y) = (AB, Ay + x)','encre','m')
box(ax,50,32,36,9,'sujet',label=r'1. $AB$ : demi-tour',size='s')
box(ax,50,21,36,9,'sujet',label=r'2. $Ay=(0\,;\,1)$',size='s')
box(ax,50,10,36,9,'resultat',label=r'3. $Ay+x=(2\,;\,1)$',size='s')
save(fig,'73-108')
