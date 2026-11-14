import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(60)
y=42
f=lambda v:8+(v-3)*68
line(ax,[(8,y),(76,y)],'fixe')
for v in (3.0625,3.125):
    disc(ax,f(v),y,1.0,'varie')
for v,rl in ((3,'sujet'),(3.25,'varie'),(3.5,'varie'),(4,'sujet')):
    disc(ax,f(v),y,2.2,rl)
text(ax,f(3),y-6,'3','sujet'); text(ax,f(4),y-6,'4','sujet')
text(ax,f(3.25),y-6,'3,25','varie'); text(ax,f(3.5),y-6,'3,5','varie')
text(ax,f(3.5),y+8,'milieu de 3 et 4','varie')
text(ax,f(3.25)-4,y-13,'milieu de 3 et 3,5','varie')
arrow(ax,(f(3.5),y+5.5),(f(3.5),y+3),'varie')
text(ax,44,20,'3 < 4 est vrai','resultat')
text(ax,44,12,'aucun nombre juste au-dessus','limite')
text(ax,44,5,'donc aucun trait de recouvrement','limite','s')
save(fig,'79-033')
