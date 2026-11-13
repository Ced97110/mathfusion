import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

def sq(ax,x,y,s,role):
    poly(ax,[(x,y),(x+s,y),(x+s,y+s),(x,y+s)],role,lw=0.5)

fig,ax=canvas(74)
text(ax,44,71,'comme « 3 fois par jour »','fixe','s')
# 3 × 5 : le signe lu morceau par morceau
text(ax,30,64,'3','varie','l')
text(ax,44,64,'×','sujet','l')
text(ax,58,64,'5','autre','l')
text(ax,18,57,'combien de fois','varie','s')
text(ax,44,57,'« fois »','sujet','m')
text(ax,68,57,'quoi prendre','autre','s')
line(ax,[(18,59),(29,62)],'varie',lw=0.6)
line(ax,[(68,59),(59,62)],'autre',lw=0.6)
# trois rangées de 5 carrés de 4 mm (5 pris 3 fois)
for yb in (42,36,30):
    for i in range(5):
        sq(ax,36+4*i,yb,4,'autre')
# compte des fois : 1, 2, 3
for yc,n in ((44,'1'),(38,'2'),(32,'3')):
    disc(ax,30,yc,1.8,'varie',label=n,size='s')
# addition
arrow(ax,(46,28),(46,22),'varie')
text(ax,44,16,'5 + 5 + 5 = 15','resultat','l')
save(fig,'03-018')
