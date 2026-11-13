import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

def sq(ax,x,y,s,role):
    poly(ax,[(x,y),(x+s,y),(x+s,y+s),(x,y+s)],role,lw=0.5)

fig,ax=canvas(62)
S=4.5
# état avant : 4 rangées × 6 carreaux, coin (6, 30) ; rangée du haut = orange
for r in range(4):
    for c in range(6):
        sq(ax,6+c*S,30+r*S,S,'varie' if r==3 else 'sujet')
text(ax,19.5,52,'4 rangées de 6','encre','s')
# état après : 6 rangées × 4 carreaux, coin (60, 25) ; ancienne rangée du haut = colonne de droite
for r in range(6):
    for c in range(4):
        sq(ax,60+c*S,25+r*S,S,'varie' if c==3 else 'sujet')
text(ax,69,56,'6 rangées de 4','encre','s')
arrow(ax,(34,44),(59,44),'varie',curve=-0.3)
text(ax,46.5,53,'quart de tour','varie','s')
text(ax,19.5,19,'4 × 6 = 6+6+6+6','sujet','m')
text(ax,69,19,'6 × 4 = 4+4+4+4+4+4','sujet','m')
text(ax,19.5,13,'24 carreaux','resultat','s')
text(ax,69,13,'24 carreaux','resultat','s')
text(ax,44,5,'4 × 6 = 6 × 4','resultat','l')
save(fig,'03-012')
