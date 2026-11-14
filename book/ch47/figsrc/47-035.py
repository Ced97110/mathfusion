import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,s=24,33,17
poly(ax,[(cx-s,cy-s),(cx+s,cy-s),(cx+s,cy+s),(cx-s,cy+s)],'fixe')
a,b=11,6
pts=[(a,b),(-b,a),(-a,-b),(b,-a)]
for i,(x,y) in enumerate(pts):
    disc(ax,cx+x,cy+y,1.8,'sujet' if i==0 else 'fixe',fill=(i==0))
disc(ax,cx,cy,1.8,'autre')
text(ax,cx+a+4,cy+b+3,'P','sujet','m')
text(ax,cx-4.5,cy-3.5,'O','autre','m')
arrow(ax,(cx+1.5,cy+1),(cx+a-2,cy+b-0.5),'limite')
text(ax,cx+9,cy-3,'×','limite','l')
box(ax,52,36,34,22,'autre')
text(ax,69,52,'O reste en place','autre','s')
text(ax,69,46,'pour les 4 rotations','autre','s')
text(ax,69,40,'(identité comprise)','autre','s')
box(ax,52,6,34,22,'limite')
text(ax,69,22,'aucune rotation','limite','s')
text(ax,69,16,"n'envoie $O$ sur $P$",'limite','s')
text(ax,69,10,'donc 2 orbites au moins','limite','s')
save(fig,'47-035')
