import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
text(ax,44,62,'16 500 et 17 500 : égalité','encre','l')
line(ax,[(8,36),(80,36)],'fixe')
for x,l in ((8,'16 000'),(44,'17 000'),(80,'18 000')):
    line(ax,[(x,34.8),(x,37.2)],'fixe',lw=0.8); text(ax,x,32.6,l,'fixe','s')
for x,l in ((26,'16 500'),(62,'17 500')):
    disc(ax,x,36,1.2,'encre',fill=False); text(ax,x,32.6,l,'encre','s')
arrow(ax,(26,38),(44,38),'sujet',curve=-0.5); arrow(ax,(62,38),(80,38),'sujet',curve=-0.5)
text(ax,44,49,'haut : 17 000 et 18 000','sujet','m')
arrow(ax,(26,29.5),(8,29.5),'autre',curve=-0.5); arrow(ax,(62,29.5),(80,29.5),'autre',curve=0.5)
text(ax,44,19,'pair : 16 000 et 18 000','autre','m')
text(ax,19,11,'6 est pair : on garde 6','autre','s'); text(ax,68,11,'7 impair : on va à 8','autre','s')
poly(ax,[(17,17.5),(18,15.5),(17,13.5),(16,15.5)],'limite')
save(fig,'01-112')
