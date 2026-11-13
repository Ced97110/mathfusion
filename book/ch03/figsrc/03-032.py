import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

from matplotlib.patches import Rectangle
fig,ax=canvas(50)
text(ax,34.2,46,'4 dans 48 : 4 dizaines = 40','varie','s',ha='right')
text(ax,2.5,40.5,nb('326 × 4 = 1 304 dizaines'),'sujet','s',ha='left')
text(ax,17,34,'avec décalage','resultat','m'); text(ax,71,34,'sans décalage','limite','m')
ax.add_patch(Rectangle((34.45,7),3.03,18.2,fc=FILL['varie'],ec=COL['varie'],lw=0.8,zorder=1))
arrow(ax,(35.96,46.2),(35.96,26.6),'varie',lw=1.3)
text(ax,35.96,3.6,'dizaines','varie','s')
text(ax,40,23,'2 6 0 8','encre','l',ha='right'); text(ax,36.97,17,'1 3 0 4','sujet','l',ha='right')
text(ax,11,17,nb('vaut 13 040'),'sujet','s')
line(ax,[(22,13.5),(41,13.5)],'encre',lw=0.8); text(ax,40,9,'1 5 6 4 8','resultat','l',ha='right',weight='bold')
text(ax,80,23,'2 6 0 8','encre','l',ha='right'); text(ax,80,17,'1 3 0 4','limite','l',ha='right')
text(ax,56,17,nb('vaut 1 304'),'limite','s')
line(ax,[(64,13.5),(81,13.5)],'limite',lw=0.8); text(ax,80,9,'3 9 1 2','limite','l',ha='right',weight='bold')
save(fig,'03-032')
