import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
O=(44,40); u=7
def Q(x,y,z): return iso(x,y,z,O,u)
A=[Q(-3,0,-2),Q(3,0,-2),Q(3,0,2),Q(-3,0,2)]
B=[Q(0,-3,-2),Q(0,3,-2),Q(0,3,2),Q(0,-3,2)]
ax.add_patch(Polygon(A,closed=True,ec=COL['sujet'],fc=FILL['sujet'],lw=0.9,zorder=2,alpha=0.85))
ax.add_patch(Polygon(B,closed=True,ec=COL['autre'],fc=FILL['autre'],lw=0.9,zorder=2.1,alpha=0.7))
line(ax,[Q(0,0,-2),Q(0,0,2)],'varie',lw=2.4)
disc(ax,*O,1.3,'encre')
text(ax,2,74,'autre plan\n= une « droite »','autre','s',ha='left')
text(ax,86,74,'plan par l’origine\n= une « droite »','sujet','s',ha='right')
text(ax,44,7,'leur droite commune = un « point »','varie','s')
arrow(ax,(44,11),(44,25),'varie',lw=0.7)
save(fig,'80-015')
