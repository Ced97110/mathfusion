import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'$G$ : les quarts de tour','fixe','m')
cx,cy=24,31
poly(ax,[(cx-18,cy-18),(cx+18,cy-18),(cx+18,cy+18),(cx-18,cy+18)],'fixe')
pts=[(10,4),(-4,10),(-10,-4),(4,-10)]
for px,py in pts: disc(ax,cx+px,cy+py,1.8,'sujet')
disc(ax,cx,cy,1.8,'autre')
text(ax,cx+10+4,cy+4,r'$x$','sujet','m'); text(ax,cx-4,cy+10+4,r'$y$','sujet','m'); text(ax,cx+4,cy-1.0,r'$O$','autre','m')
text(ax,24,7,'4 points : une orbite','sujet','s')
text(ax,66,42,r'$Gx=Gy$','resultat','l'); text(ax,66,36,'même orbite','resultat','s')
text(ax,66,22,r'$Gx\neq GO$','limite','l'); text(ax,66,16,'orbites différentes','limite','s')
save(fig,'47-055')
