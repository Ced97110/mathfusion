import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
X=lambda r:6+7*(r-2)
def domino(r,base,h,role): box(ax,X(r)-1.5,base,3,h,role,r=0.5)
# haut
text(ax,3,76,'ordinaire : par le voisin','autre','m',ha='left')
line(ax,[(3,59),(85,59)],'fixe')
for r in range(2,13): domino(r,59,9,'fixe')
for r in range(2,12):
    p=(X(r)+1,68.5); q=(X(r+1)-1,68.5)
    arrow(ax,p,q,'autre',lw=1.4 if r==11 else 1.0,curve=-0.5)
text(ax,69,56,'11','fixe','s'); text(ax,76,56,'12','fixe','s')
# bas
text(ax,3,51,'ici : par ses facteurs','varie','m',ha='left')
line(ax,[(3,14),(85,14)],'fixe')
for r in range(2,13): domino(r,14,10,'sujet' if r==12 else 'varie' if r in (3,4) else 'fixe')
for s,x,role in (('3',13,'varie'),('4',20,'varie'),('11',69,'fixe'),('12',76,'sujet')): text(ax,x,10.5,s,role,'s')
arrow(ax,(13,24.5),(76,24.5),'varie',lw=1.3,curve=-2*18.5/63)
arrow(ax,(20,24.5),(76,24.5),'varie',lw=1.3,curve=-2*12.5/56)
text(ax,45,46.5,'3 × 4 = 12','varie','m',weight='bold')
brace(ax,25.5,70.5,8,'fixe',label='5 à 11 : aucun rôle')
save(fig,'01-159')
