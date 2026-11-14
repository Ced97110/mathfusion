import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arcarr(ax,c,r,a0,a1,role,lw=1.0):
    n=24; pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw); arrow(ax,pts[-2],pts[-1],role,lw)

fig,ax=canvas(76); s=5.5; OL=(22,40); OR=(66,40)
def pl(o,x,y): return (o[0]+s*x,o[1]+s*y)
for o in (OL,OR):
    line(ax,[pl(o,-3.8,0),pl(o,3.8,0)],'fixe',lw=0.5); line(ax,[pl(o,0,-3.8),pl(o,0,3.8)],'fixe',lw=0.5)
line(ax,[pl(OL,-3.5,-3.5),pl(OL,3.5,3.5)],'sujet',lw=1.3)
disc(ax,*pl(OL,3,2),1.1,'encre'); disc(ax,*pl(OL,2,3),1.1,'varie')
arrow(ax,pl(OL,2.9,2.3),pl(OL,2.4,2.8),'varie',curve=0.9); arrow(ax,pl(OL,2.2,2.8),pl(OL,2.8,2.2),'varie',curve=0.9)
text(ax,OL[0]+s*3+2,OL[1]+s*2-3,'(3 ; 2)','encre','s',ha='left'); text(ax,OL[0]+s*2,OL[1]+s*3+4,'(2 ; 3)','varie','s')
line(ax,[pl(OR,-3.5,0),pl(OR,3.8,0)],'sujet',lw=1.3); line(ax,[pl(OR,-3.5,-3.5),pl(OR,3.5,3.5)],'autre',lw=1.3)
A=pl(OR,3,2);C=pl(OR,3,-2);D=pl(OR,-2,3)
disc(ax,*A,1.1,'encre'); disc(ax,*C,1.1,'varie'); disc(ax,*D,1.1,'limite')
arrow(ax,(A[0],A[1]-1.5),(C[0],C[1]+1.5),'varie'); arrow(ax,(C[0]-1.5,C[1]+0.8),(D[0]+0.8,D[1]-1.5),'limite')
text(ax,A[0]-1,A[1]+3.5,'(3 ; 2)','encre','s'); text(ax,C[0]-1,C[1]-3.5,'(3 ; −2)','varie','s',ha='right'); text(ax,D[0],D[1]+3.5,'(−2 ; 3)','limite','s')
text(ax,OL[0],70,'même miroir, deux fois','sujet','s'); text(ax,OR[0],70,'deux miroirs différents','autre','s')
text(ax,OL[0],8,'retour au départ','resultat','m'); text(ax,OR[0],8,'pas de retour','limite','m')
save(fig,'73-100')
