import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

def plus(ax,x,y,r=1.2):
    line(ax,[(x-r,y),(x+r,y)],'encre',lw=0.8)
    line(ax,[(x,y-r),(x,y+r)],'encre',lw=0.8)

fig,ax=canvas(78)
# ligne A : quatre 6, accolade, 4
for x in (14,28,42,56):
    box(ax,x,64,8,7,'fixe',label='6',size='m')
for x in (25,39,53):
    plus(ax,x,67.5)
text(ax,67,67.5,'les termes','fixe','s',ha='left')
brace(ax,14,64,62,'sujet',down=True)
text(ax,39,57,'4','sujet','l')
text(ax,50,57,'le compte des termes','sujet','s',ha='left')
# ligne B : 6, points cachés, 6, 6, accolade, 426
for x in (14,28,56):
    box(ax,x,30,8,7,'fixe',label='6',size='m')
for x in (44,46,48):
    ax.add_patch(Circle((x,33.5),0.45,fc=COL['encre'],ec=COL['encre'],lw=0.3,zorder=3))
for x in (25,39,53):
    plus(ax,x,33.5)
box(ax,41,29,10,9,'limite',fill=False,dash=True)
text(ax,46,41,'termes cachés','limite','s')
brace(ax,14,64,28,'sujet',down=True)
text(ax,39,23,'426','sujet','l')
text(ax,50,23,'l’accolade le dit','sujet','s',ha='left')
save(fig,'03-015')
