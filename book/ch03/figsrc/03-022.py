import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

def sq(ax,x,y,s,role):
    poly(ax,[(x,y),(x+s,y),(x+s,y+s),(x,y+s)],role,lw=0.4)

fig,ax=canvas(78)
line(ax,[(44,8),(44,76)],'fixe',lw=0.6)
text(ax,22.5,72,'3 × 5','encre','l')
text(ax,65.5,72,'5 × 3','encre','l')
text(ax,22.5,64,'multiplicande 5','autre','s')
text(ax,65.5,64,'multiplicande 3','autre','s')
# gauche : 3 barres de 5 carrés de 3 mm (le 5 répété 3 fois)
for y in (56,51,46):
    for i in range(5):
        sq(ax,15+3*i,y,3,'autre')
for yc in (57.5,52.5,47.5):
    disc(ax,11,yc,1.2,'sujet')
text(ax,22.5,31,'multiplicateur 3','sujet','s')
# droite : 5 barres de 3 carrés (le 3 répété 5 fois)
for y in (56,51,46,41,36):
    for i in range(3):
        sq(ax,62+3*i,y,3,'autre')
for yc in (57.5,52.5,47.5,42.5,37.5):
    disc(ax,58,yc,1.2,'sujet')
text(ax,65.5,31,'multiplicateur 5','sujet','s')
# même produit, 15
text(ax,22.5,22,'produit : 15','resultat','m')
text(ax,65.5,22,'produit : 15','resultat','m')
text(ax,44,4,'même produit, autre rôle','encre','s')
save(fig,'03-022')
