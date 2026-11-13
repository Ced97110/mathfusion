import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(58)
u=18; A=(8,8); C=(80,8); O=(44,8); R=36
arcpts=[(O[0]-R*math.cos(math.radians(a)),8+R*math.sin(math.radians(a))) for a in [i*180/60 for i in range(61)]]
line(ax,arcpts,'fixe',0.8); line(ax,[A,C],'fixe',0.8)
D=(26,8); B=(26,8+math.sqrt(3)*u)
poly(ax,[O,D,B],'sujet')
line(ax,[O,B],'varie',1.6); line(ax,[D,B],'resultat',1.8); line(ax,[D,O],'fixe',1.6)
line(ax,[(26,10.2),(28.2,10.2),(28.2,8)],'fixe',0.7)
for p,r in [(A,'fixe'),(C,'fixe'),(O,'sujet'),(D,'fixe'),(B,'resultat')]: disc(ax,p[0],p[1],1.2,r)
for p,n,dx,dy in [(A,'A',0,-4),(C,'C',0,-4),(D,'D',-1,-4),(O,'O',1,-4),(B,'B',-4,3.5)]: text(ax,p[0]+dx,p[1]+dy,r'$'+n+'$')
text(ax,40.5,24.5,r'$R$ = 2','varie')
text(ax,34,12.5,r'$OD$ = 1','fixe','s')
text(ax,20,24,r'$DB$','resultat')
text(ax,67,53,r'$DB^2 = R^2 - OD^2$','resultat','m')
text(ax,67,46,r'= 4 − 1 = 3','resultat','m')
save(fig,'61-213')
