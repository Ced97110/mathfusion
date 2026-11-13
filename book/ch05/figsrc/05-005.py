import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(66)
u=3.6; x0=14
def planche(y,L,piece,role,lab,reste=0):
    text(ax,2,y+2.5,lab,'encre','s',ha='left')
    n=L//piece
    for i in range(n): box(ax,x0+i*piece*u,y,piece*u,5,role,r=0.5)
    if reste:
        box(ax,x0+n*piece*u,y,reste*u,5,'limite',r=0.5)
        text(ax,x0+n*piece*u+reste*u,y-2.8,'reste 2 cm','limite','s',ha='right')
text(ax,2,62,'6 cm : ça tombe juste','resultat','m',ha='left')
planche(50,12,6,'resultat','12 cm'); planche(41,18,6,'resultat','18 cm')
text(ax,2,31,'4 cm : il reste 2 cm','limite','m',ha='left')
planche(19,12,4,'resultat','12 cm'); planche(8,18,4,'resultat','18 cm',reste=2)
save(fig,'05-005')
