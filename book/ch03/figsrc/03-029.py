import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

from matplotlib.patches import Rectangle
fig,ax=canvas(70)
ax.add_patch(Rectangle((8,22),60,36,fc=FILL['sujet'],ec='none',zorder=2))
ax.add_patch(Rectangle((68,22),12,36,fc=FILL['sujet'],ec='none',zorder=2))
line(ax,[(68,22),(68,58)],'sujet',lw=0.5)
ax.add_patch(Rectangle((8,22),72,36,fc='none',ec=COL['resultat'],lw=1.4,zorder=3))
text(ax,4.5,40,'326','resultat','s',rot=90)
text(ax,38,45.5,'produit partiel','sujet','s'); text(ax,38,31.5,'326 × 40','sujet','s'); text(ax,38,26,nb('13 040'),'sujet','m',weight='bold')
text(ax,74,45.5,'produit partiel','sujet','s',rot=90); text(ax,74,31.5,'326 × 8','sujet','s'); text(ax,74,26,nb('2 608'),'sujet','m',weight='bold')
for a,b in [(8,68),(68.6,80)]:
    line(ax,[(a,19),(b,19)],'varie',lw=1.6); line(ax,[(a,18.4),(a,19.6)],'varie',lw=1.0); line(ax,[(b,18.4),(b,19.6)],'varie',lw=1.0)
text(ax,38,14.5,'morceau 40','varie','m'); text(ax,74,14.5,'morceau 8','varie','m')
brace(ax,8,80,59.5,'resultat',label=None,down=False); text(ax,44,64,nb('produit total : 15 648'),'resultat','m')
save(fig,'03-029')
