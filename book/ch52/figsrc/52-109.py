import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
for y,h,r,t in ((54,10,'sujet',r'$M=(7)$ maximal, $a=3\notin M$'),(14,10,'resultat',r'$1\in I$ : 3 a un inverse')):
    box(ax,24,y,62,h,r,label=t,size='s')
box(ax,24,31,62,16,'varie')
text(ax,55,42,'I contient M et 3','varie','s')
text(ax,55,36,'M maximal : I = ℤ','varie','s')
for y0,y1 in ((54,47),(31,24)):
    arrow(ax,(55,y0),(55,y1),'fixe')
text(ax,2,59,'départ','sujet','s',ha='left'); text(ax,2,39,'étape clé','varie','s',ha='left'); text(ax,2,19,'arrivée','resultat','s',ha='left')
save(fig,'52-109')
