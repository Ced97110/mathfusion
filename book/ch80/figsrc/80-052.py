import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,28,64,32,11,'resultat',label='plan entier')
for i,x in enumerate((3,28,53)):
    box(ax,x,34,22,11,'sujet',label='droite')
    line(ax,[(x+11,45),(44,64)],'fixe'); line(ax,[(44,23),(x+11,34)],'fixe')
box(ax,28,12,32,11,'fixe',label='origine seule')
arrow(ax,(84,14),(84,70),'varie')
text(ax,79,42,'contenu dans','varie','s',ha='center',rot=90)
text(ax,44,4,'inclusion : du plus petit au plus grand','encre','s')
save(fig,'80-052')
