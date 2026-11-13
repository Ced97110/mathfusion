import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(56)
t=4
text(ax,4,53,'7 carreaux','encre','l',ha='left')
tiles(ax,4,44,1,7,t,'resultat')
text(ax,36,46,'1 rangée de 7 : ça marche','resultat','s',ha='left')
tiles(ax,4,30,2,3,t); tiles(ax,4+3*t+2,30,1,1,t,'limite')
text(ax,36,34,'2 rangées : il reste 1','limite','s',ha='left')
tiles(ax,4,10,3,2,t); tiles(ax,4+2*t+2,10,1,1,t,'limite')
text(ax,36,16,'3 rangées : il reste 1','limite','s',ha='left')
save(fig,'05-002')
