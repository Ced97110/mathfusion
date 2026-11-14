import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,21,71,'Léa','sujet','m'); text(ax,66,71,'Tom','autre','m')
disc(ax,15,60,3,'sujet'); disc(ax,27,60,3,'sujet')
text(ax,21,52,'2 générateurs','sujet','s')
for k in range(3): box(ax,5+k*11,38,10,5,'fixe')
text(ax,21,32,'3 relations','fixe','s')
c=3
for i in range(8):
    for j in range(8):
        ax.add_patch(Rectangle((54+i*c,43+j*c),c,c,ec=COL['autre'],fc=FILL['autre'],lw=0.5,zorder=2))
text(ax,66,37,'64 cases','autre','s')
for k in range(8): disc(ax,26.5+k*5,14,2.2,'resultat')
arrow(ax,(21,28),(35,18),'fixe'); arrow(ax,(66,34),(53,18),'fixe')
text(ax,44,5,'mêmes 8 positions','resultat','s')
save(fig,'49-008')
