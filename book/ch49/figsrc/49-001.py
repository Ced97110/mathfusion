import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
c=3.2
for i in range(8):
    for j in range(8):
        ax.add_patch(Rectangle((4+i*c,22+j*c),c,c,ec=COL['fixe'],fc=FILL['fixe'],lw=0.5,zorder=2))
text(ax,17,52,'Tableau complet','fixe','s')
text(ax,17,16,'64 cases','fixe','m')
arrow(ax,(33,35),(46,35),'varie',lw=1.4)
text(ax,64,55,'Message','sujet','s')
disc(ax,56,46,3.2,'sujet',label=r'$r$')
disc(ax,72,46,3.2,'autre',label=r'$s$')
text(ax,64,38,'2 lettres','sujet','s')
for k in range(3):
    box(ax,50+k*11.5,22,10,7,'fixe',label='règle',size='s')
text(ax,64,17,'3 règles','fixe','m')
save(fig,'49-001')
