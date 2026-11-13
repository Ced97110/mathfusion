import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(50)
t=2.2
for y,n in [(40,12),(28,7),(16,20)]:
    text(ax,2,y,str(n),'sujet','m',ha='left')
    tiles(ax,12,y-t/2,1,n,t)
    arrow(ax,(58,y),(66,28),'varie')
box(ax,66,21,18,14,'varie',label=r'$n$',size='xl')
text(ax,75,17,'tout nombre','varie','s')
text(ax,75,10,r'$n=12$ ou $n=7$','encre','s')
save(fig,'05-008')
