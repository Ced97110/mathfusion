import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,21.25,56,'une colonne donne 19','encre','s'); text(ax,65.25,56,'une colonne donne 33','encre','s')
def sq(x0,y,n,role):
    for i in range(n): box(ax,x0+3.5*i,y,3,3,role,r=0.5)
sq(4,47,10,'sujet'); sq(4,43.4,9,'resultat')
for y,n,r in [(47,10,'sujet'),(43.4,10,'sujet'),(39.8,10,'sujet'),(36.2,3,'resultat')]: sq(48,y,n,r)
box(ax,3.5,46.75,35.5,3.5,'varie',fill=False,lw=1.1,r=0.5)
for y in (46.75,43.15,39.55): box(ax,47.5,y,35.5,3.5,'varie',fill=False,lw=1.1,r=0.5)
text(ax,21.25,29,'1 paquet de dix : retenue 1','varie','s'); text(ax,65.25,29,'3 paquets de dix : retenue 3','varie','s')
text(ax,21.25,24,'on garde 9','resultat','s'); text(ax,65.25,24,'on garde 3','resultat','s')
text(ax,21.25,17,'deux nombres : au plus 19','fixe','s'); text(ax,65.25,17,'plus de deux nombres','fixe','s')
save(fig,'02-028')
