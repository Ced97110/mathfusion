import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,2,40,84,38,'sujet',fill=False,dash=True,lw=1.1)
text(ax,44,73,'noyau : diagonales fixes','sujet','m',weight='bold')
for (x,y,l) in [(5,56,'neutre'),(46,56,'demi-tour'),(5,44,'réflexion diagonale 1'),(46,44,'réflexion diagonale 2')]:
    box(ax,x,y,38,9,'sujet',label=l,size='s')
box(ax,2,2,84,34,'varie',fill=False,dash=True,lw=1.1)
text(ax,44,31,'diagonales échangées','varie','m',weight='bold')
for (x,y,l) in [(5,18,'quart de tour'),(46,18,'trois quarts de tour'),(5,6,'autre réflexion'),(46,6,'autre réflexion')]:
    box(ax,x,y,38,9,'varie',label=l,size='s')
save(fig,'49-110')
