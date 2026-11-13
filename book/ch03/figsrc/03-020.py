import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

fig,ax=canvas(62)
line(ax,[(44,10),(44,60)],'fixe',lw=0.6)
text(ax,22.5,57,'3 + 5','autre','l')
text(ax,65.5,57,'3 × 5','sujet','l')
# panneau gauche : 3 + 5 mis bout à bout = 8 disques en une rangée
for x in [7,11,15,21,25,29,33,37]:
    disc(ax,x,44,1.2,'fixe')
box(ax,4.5,41,35,6,'autre',fill=False)
text(ax,22.5,30,'somme : 8','autre','m')
# panneau droit : 3 rangées de 5 disques = 15
for y in (50,45,40):
    for i in range(5):
        disc(ax,57.5+4*i,y,1.2,'fixe')
box(ax,55,37.5,21,15,'sujet',fill=False)
text(ax,65.5,30,'produit : 15','sujet','m')
text(ax,22.5,22,'départ : 3 et 5','fixe','s')
text(ax,65.5,22,'facteurs : 3 et 5','fixe','s')
text(ax,65.5,14,'un nombre, pas une action','sujet','s')
save(fig,'03-020')
