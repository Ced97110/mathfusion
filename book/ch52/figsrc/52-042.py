import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,14,48,60,13,'sujet',label=r'$I$ absorbe',size='m',weight='bold')
box(ax,6,1,76,15,'resultat',label='la multiplication des paquets\na un sens',size='s')
arrow(ax,(40,48),(40,17),'varie',lw=1.2); arrow(ax,(48,17),(48,48),'varie',lw=1.2)
text(ax,21,32,'absorber suffit','varie','s'); text(ax,68,32,'absorber est nécessaire','varie','s')
save(fig,'52-042')
