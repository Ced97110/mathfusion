import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

from matplotlib.patches import Rectangle
fig,ax=canvas(54)
text(ax,50,48,'3 2 6','encre','l',ha='right')
text(ax,48.99,40,'8','varie','l',weight='bold'); text(ax,45.96,40,'4','varie','l',weight='bold'); text(ax,36.87,40,'×','encre','l')
line(ax,[(34,36.5),(51,36.5)],'encre',lw=0.8)
ax.add_patch(Rectangle((41.4,37.6),3.05,4.8,fc='none',ec=COL['limite'],ls='--',lw=0.8,zorder=2))
text(ax,16,45,'pas de 3e chiffre','limite','s'); line(ax,[(27.5,44.5),(41.4,41.5)],'limite',lw=0.6)
text(ax,50,32,'2 6 0 8','sujet','l',ha='right'); text(ax,50,24,'1 3 0 4 0','sujet','l',ha='right')
arrow(ax,(50.5,38.5),(51,33.6),'varie',curve=-0.6)
arrow(ax,(46,42.2),(51.5,25.5),'varie',curve=-0.8)
for y,s in [(32,'1. le chiffre 8'),(24,'2. le chiffre 4'),(16,'3. on additionne')]: text(ax,60,y,s,'encre','s',ha='left')
line(ax,[(34,20.5),(51,20.5)],'resultat',lw=0.8); text(ax,50,16,'1 5 6 4 8','resultat','l',ha='right',weight='bold')
text(ax,44,7,'48 a 2 chiffres : 2 lignes','sujet','s')
save(fig,'03-031')
