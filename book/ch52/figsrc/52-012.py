import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,16,80,'entier','fixe','s'); text(ax,72,80,'reste par 4','fixe','s')
box(ax,2,40,28,36,'sujet',fill=False,dash=True)
text(ax,16,72,'noyau','sujet','s',weight='bold')
ys=[(64,'12'),(57,'8'),(50,'4'),(43,'0')]
for y,n in ys:
    disc(ax,16,y,3.2,'sujet',label=n)
    arrow(ax,(19.4,y),(68.6,52+(y-53.5)*0.12),'sujet',lw=0.8)
for y,n,r in [(26,'5','fixe'),(12,'6','fixe')]:
    disc(ax,16,y,3.2,r,label=n)
disc(ax,72,52,3.2,'sujet',label='0')
for y,n in [(26,'1'),(12,'2')]:
    disc(ax,72,y,3.2,'fixe',label=n)
arrow(ax,(19.4,26),(68.6,26),'fixe'); arrow(ax,(19.4,12),(68.6,12),'fixe')
text(ax,44,4,'quelle sorte de partie ?','sujet','s')
save(fig,'52-012')
