import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,3,58,'chaque case grise vaut 4','encre','s',ha='left')
for y,t in ((51,'3 termes'),(40,'4 termes'),(27,'426 termes')): text(ax,3,y,t,'encre','s',ha='left')
for yc,xs in ((51,(17,26,35)),(40,(17,26,35,44)),(27,(17,26,35,53))):
    for x in xs: box(ax,x,yc-3,6,6,'fixe',r=0.4)
for yc,xs in ((51,(24.5,33.5)),(40,(24.5,33.5,42.5)),(27,(24.5,33.5,42.5,51.25))):
    for x in xs: disc(ax,x,yc,0.9,'varie')
for x in (45,47,49): disc(ax,x,27,0.5,'fixe')
for y,t in ((51,'2 additions'),(40,'3 additions'),(19,'425 additions')): text(ax,86,y,t,'varie','s',ha='right')
for x,y,t in ((44,51,'= 12'),(53,40,'= 16'),(62,27,'= 1 704')): text(ax,x,y,t,'resultat','m',ha='left')
text(ax,86,12,"425 occasions d'erreur",'limite','s',ha='right',weight='bold')
save(fig,'03-002')
