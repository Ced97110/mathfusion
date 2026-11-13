import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(38)
t=3; gap=6; x=5; y=18
for rows,cols in [(1,12),(2,6),(3,4)]:
    tiles(ax,x,y,rows,cols,t)
    text(ax,x+cols*t/2,13,rf'${rows} \times {cols}$','sujet','m')
    x+=cols*t+gap
text(ax,44,33,'toujours 12 carreaux, sans trou','resultat','m')
save(fig,'05-001')
