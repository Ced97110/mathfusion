import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
for x,s in ((27,'unités'),(47,'dixièmes'),(61,'centièmes')): text(ax,x,63,s,'encre','s')
cols=((20,14),(40,14),(54,14))
for y,role,ds in ((41,'fixe','347'),(31,'fixe','285'),(19,'resultat','632')):
    for (x,w),d in zip(cols,ds): box(ax,x,y,w,9,role,label=d,size='l')
line(ax,[(10,35.5),(14,35.5)],'encre',lw=1.2); line(ax,[(12,33.5),(12,37.5)],'encre',lw=1.2)
line(ax,[(10,29.5),(70,29.5)],'encre',lw=1.0)
line(ax,[(37,16),(37,58)],'sujet',lw=0.6,dash=True)
for y in (43.8,33.8,21.8):
    ax.add_patch(Circle((37,y),0.9,ec=COL['encre'],fc=COL['encre'],zorder=4)); ax.add_patch(Polygon([(36.2,y-0.3),(37.8,y-0.3),(36.7,y-2.6)],closed=True,ec=COL['encre'],fc=COL['encre'],zorder=4))
text(ax,47,54,'1','varie','s'); text(ax,27,54,'1','varie','s')
arrow(ax,(60,51),(49,54),'varie',curve=0.3); arrow(ax,(44,51),(29,54),'varie',curve=0.3)
save(fig,'02-085')
