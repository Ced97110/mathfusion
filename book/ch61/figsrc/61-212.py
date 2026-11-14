import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(58)
u=18; A=(8,8); C=(80,8); O=(44,8); R=36
arcpts=[(O[0]-R*math.cos(math.radians(a)),8+R*math.sin(math.radians(a))) for a in [i*180/60 for i in range(61)]]
poly(ax,arcpts,'sujet')
line(ax,[A,C],'fixe',1.2)
D=(26,8); B=(26,8+math.sqrt(3)*u)
line(ax,[D,B],'resultat',1.8)
line(ax,[(26,10.2),(28.2,10.2),(28.2,8)],'fixe',0.7)
for p,r in [(A,'fixe'),(C,'fixe'),(D,'varie'),(B,'resultat')]: disc(ax,p[0],p[1],1.3,r)
for p,n,dx,dy in [(A,'A',0,-4),(C,'C',0,-4),(D,'D',0,-4),(B,'B',-4,3.5)]: text(ax,p[0]+dx,p[1]+dy,r'$'+n+'$')
text(ax,17,12,'1','fixe'); text(ax,53,12,r'$a$','sujet')
text(ax,22.5,23.6,r'$x$','resultat','l')
text(ax,60,52,r'$x^2 = a$','resultat','l')
save(fig,'61-212')
