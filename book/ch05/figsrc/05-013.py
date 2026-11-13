import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(40)
f=numberline(ax,6,76,14,0,20,1,every=4)
disc(ax,f(0),14,1.5,'limite',fill=False)
for k in range(1,6):
    disc(ax,f(4*k),14,1.5,'sujet')
    arrow(ax,(f(4*(k-1))+1.5,15.5),(f(4*k)-1.5,15.5),'varie',curve=-0.5)
    text(ax,(f(4*(k-1))+f(4*k))/2,23,rf'$\times {k}$','varie','s')
text(ax,44,34,'les multiples de 4','sujet','m')
text(ax,f(0),5,'0 : exclu','limite','s',ha='left')
save(fig,'05-013')
