import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(62)
cx,cy=44,30; t=math.radians(30); d=(math.cos(t),math.sin(t))
line(ax,[(cx-40*d[0],cy-40*d[1]),(cx+40*d[0],cy+40*d[1])],'fixe',lw=1.2)
disc(ax,cx,cy,1.2,'fixe')
v=(cx+14*d[0],cy+14*d[1]); w2=(cx+28*d[0],cy+28*d[1])
disc(ax,v[0],v[1],1.6,'sujet'); disc(ax,w2[0],w2[1],1.6,'varie')
arrow(ax,(v[0]+1,v[1]+1.5),(w2[0]-1,w2[1]+1.5),'varie',curve=0.0)
text(ax,v[0],v[1]-5,r'$v$','sujet','m'); text(ax,w2[0],w2[1]-5,r'$2v$','varie','m')
text(ax,cx-2,cy-5,'origine','fixe','s'); text(ax,20,52,'la droite reste en place','resultat','s')
save(fig,'80-119')
