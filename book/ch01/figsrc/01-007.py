import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
for x,t in [(15,'compter'),(44,'écrire court'),(73,'simplifier')]:
    text(ax,x,63,t,'varie','m')
    arrow(ax,(x,59),(x,55),'fixe')
    arrow(ax,(x,37),(x,30),'fixe')
for x,t in [(15,'les entiers'),(44,'la position'),(73,"l'arrondi")]:
    text(ax,x,25,t,'resultat','m')
for cx in [7.5+5*i for i in range(4)]:
    box(ax,cx-1.8,44,3.6,3.6,'fixe',r=0.5)
for i,d in enumerate('4329'):
    box(ax,33+5.5*i,41,5.5,8,'sujet' if i==0 else 'fixe',label=d,r=0.6)
line(ax,[(61,45),(83,45)],'fixe')
for x in (61,83): line(ax,[(x,43.8),(x,46.2)],'fixe',lw=0.8)
disc(ax,68.2,45,1,'sujet')
text(ax,70,50.5,'4 329','sujet','s')
arrow(ax,(68.2,47),(61,47),'varie',curve=0.4)
text(ax,61,41,'4 000','resultat','s')
text(ax,83,41,'5 000','fixe','s')
save(fig,'01-007')
