import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,21,64,'abéliens','sujet','m',weight='bold'); text(ax,67,64,'pas abélien','limite','m',weight='bold')
for y,l in [(46,'horloge à 4 h'),(33,'rotations du carré'),(20,'horloge à 6 h')]:
    box(ax,2,y,38,10,'sujet',label=l,size='s')
box(ax,48,20,38,10,'limite',label='permutations de 3 objets',size='s')
arrow(ax,(41,25),(47,25),'varie',both=True)
text(ax,44,10,'mêmes 6 éléments, mais...','varie','s')
save(fig,'45-130')
