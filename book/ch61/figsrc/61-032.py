import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,59,55,'briques du milieu','fixe','s')
text(ax,11,24,'briques\ndu haut','sujet','s')
cols=[(36,'1'),(60,'√2')]
rows=[(26,'1',['1','√2']),(12,'√3',['√3','√6'])]
for x,t in cols: box(ax,x,40,22,9,'fixe',label=t)
for y,t,cells in rows:
    box(ax,22,y,12,11,'sujet',label=t)
    for (x,_),c in zip(cols,cells): box(ax,x,y,22,11,'resultat',label=c)
text(ax,59,5,'4 produits','resultat','s')
save(fig,'61-032')
