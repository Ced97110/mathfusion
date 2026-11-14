import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arcarr(ax,c,r,a0,a1,role,lw=1.0):
    n=24; pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw); arrow(ax,pts[-2],pts[-1],role,lw)

fig,ax=canvas(66); s=20; o=(26,42)
pl=lambda x,y:(o[0]+s*x,o[1]+s*y)
line(ax,[pl(-0.5,0),pl(1.6,0)],'fixe',lw=0.5); line(ax,[pl(0,-1.4),pl(0,0.5)],'fixe',lw=0.5)
O,Pp,Rr=pl(0,0),pl(1,0),pl(0,-1)
arrow(ax,(O[0]+1.6,O[1]+2),(Pp[0]-1.6,Pp[1]+2),'sujet',lw=1.3,curve=-0.0)
arcarr(ax,O,s,-4,-86,'varie',lw=1.3)
arrow(ax,(Rr[0],Rr[1]+1.6),(O[0],O[1]-1.6),'resultat',lw=1.3)
for q,r in [(O,'encre'),(Pp,'encre'),(Rr,'fixe')]: disc(ax,*q,1.2,r)
text(ax,O[0]-3,O[1]+4,'(0 ; 0)','encre','s',ha='right'); text(ax,Pp[0]+3,Pp[1]-3,'(1 ; 0)','encre','s',ha='left'); text(ax,Rr[0]+3,Rr[1]-3,'(0 ; −1)','fixe','s',ha='left')
text(ax,36,O[1]+7,'aller : +(1 ; 0)','sujet','s'); text(ax,Pp[0]-6,Rr[1]+3,r'$A^{-1}$','varie','s',ha='left')
text(ax,O[0]-2.5,(O[1]+Rr[1])/2,'+(0 ; 1)','resultat','s',ha='right')
text(ax,70,60,r'inverse de $(A,\,x)$ :','encre','s'); text(ax,70,55,r'$(A^{-1},\,-A^{-1}x)$','sujet','m')
text(ax,70,46,r'$y=-A^{-1}x$','encre','m'); text(ax,70,40,r'$=(0\,;\,1)$','resultat','m'); text(ax,70,33,r'et non $(-1\,;\,0)$','limite','s')
text(ax,44,5,r'$(A,x)(A^{-1},y)=(I,0)$ : neutre','resultat','s')
save(fig,'73-111')
