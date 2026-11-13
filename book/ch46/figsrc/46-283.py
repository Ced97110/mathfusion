import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,54,64,'deux horloges à 2 h','encre','m')
for i in range(2):
    box(ax,30+i*26,6,22,9,'sujet',label=str(i))
    box(ax,2,22+i*22,18,18,'autre',label=str(i)) if False else None
text(ax,35,2.5,'','encre')
for j in range(2):
    box(ax,8,20+j*22,16,18,'autre',label=str(j))
for i in range(2):
    for j in range(2):
        box(ax,30+i*26,20+j*22,22,18,'resultat',label=f'{i}{j}')
text(ax,52,2.5,'1re horloge','sujet','s')
text(ax,3.5,38,'2e horloge','autre','s',rot=90)
save(fig,'46-283')
