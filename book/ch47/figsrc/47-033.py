import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cx,cy,s=22,32,17
poly(ax,[(cx-s,cy-s),(cx+s,cy-s),(cx+s,cy+s),(cx-s,cy+s)],'fixe')
a,b=11,6
pts=[(a,b),(-b,a),(-a,-b),(b,-a)]
for (x,y) in pts: disc(ax,cx+x,cy+y,1.8,'sujet')
disc(ax,cx,cy,1.8,'autre')
text(ax,cx+a+4,cy+b+3,'P','sujet','m')
text(ax,cx+4.5,cy-3.5,'O','autre','m')
box(ax,50,38,34,20,'sujet',label=None)
text(ax,67,53.5,'orbite de P','sujet','s')
for i in range(4): disc(ax,56+i*7,45,1.8,'sujet')
box(ax,50,8,34,20,'autre')
text(ax,67,23.5,r'orbite $\{O\}$','autre','s')
disc(ax,67,15,1.8,'autre')
arrow(ax,(cx+a+2,cy+b-1),(49,45),'fixe',curve=0.0)
arrow(ax,(cx+2,cy-1),(49,15),'fixe')
text(ax,cx,4.5,'1 point = 1 seule orbite','resultat','s')
save(fig,'47-033')
