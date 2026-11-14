import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(62)
cx,cy=30,32
ax.add_patch(Circle((cx,cy),21,ec=COL['sujet'],fc='none',lw=1.3,zorder=3))
hit={(-1,1),(1,0),(0,-2)}
for i in range(-3,4):
    for j in range(-3,4):
        if math.hypot(i,j)*7<=18: disc(ax,cx+7*i,cy+7*j,1.0 if (i,j) not in hit else 1.6,'varie' if (i,j) in hit else 'fixe')
text(ax,30,57,'propriété commune','sujet','m'); text(ax,30,6,'tous les tracés possibles','sujet','s')
disc(ax,58,52,1.6,'varie'); text(ax,61,52,'tracés essayés','varie','s',ha='left')
disc(ax,72,36,2.2,'limite'); text(ax,72,44,'nombre visé','limite','m'); text(ax,72,29,'hors de la propriété','limite','s')
save(fig,'61-012')
