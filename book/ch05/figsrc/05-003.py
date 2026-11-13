import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(56)
A=[(4,2,2),(6,2,3),(8,2,4),(9,3,3),(10,2,5),(12,3,4)]
B=[2,3,5,7,11]
text(ax,2,52,'ont un vrai rectangle','sujet','m',ha='left')
for i,(n,r,c) in enumerate(A):
    x=2+i*14
    box(ax,x,40,11,7,'sujet',label=str(n))
    tiles(ax,x+5.5-c,30+0.0,r,c,2)
text(ax,2,24,'rangée seulement','autre','m',ha='left')
for i,n in enumerate(B):
    box(ax,2+i*14,11,11,7,'autre',label=str(n))
save(fig,'05-003')
