import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52); s=9; OL=(8,16); OR=(52,16)
pl=lambda o,x,y:(o[0]+s*x,o[1]+s*y)
for o in (OL,OR):
    line(ax,[pl(o,-0.3,0),pl(o,3.6,0)],'fixe',lw=0.5); line(ax,[pl(o,0,-0.3),pl(o,0,2)],'fixe',lw=0.5)
for q,r in [((0,0),'sujet'),((1,1),'sujet')]:
    disc(ax,*pl(OL,*q),1.1,r); disc(ax,*pl(OR,*q),1.1,r)
for q,e in [((0,0),(2,0)),((1,1),(3,1))]:
    a,b=pl(OL,*q),pl(OL,*e); arrow(ax,(a[0]+1.4,a[1]),(b[0]-1.4,b[1]),'varie',lw=1.2); disc(ax,*b,1.1,'resultat')
for q,e in [((1,1),(2,1))]:
    a,b=pl(OR,*q),pl(OR,*e); arrow(ax,(a[0]+1.4,a[1]),(b[0]-1.4,b[1]),'varie',lw=1.2); disc(ax,*b,1.1,'autre')
disc(ax,*pl(OR,0,0),1.6,'fixe',fill=False)
text(ax,24,44,r'translation $x=(2\,;\,0)$','sujet','s'); text(ax,67,44,'cisaillement','autre','s')
text(ax,24,7,'tous : même flèche','resultat','s'); text(ax,67,7,'flèches différentes','autre','s')
save(fig,'73-106')
