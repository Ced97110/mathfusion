import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(84)
t=1.8; g=3.0
text(ax,2,81,'diviseur = nombre de rangées','fixe','s',ha='left')
def row(n,top,role,dims,head):
    # dims : liste de (rangées, colonnes) ; base des rectangles alignée
    h=max(r for r,c in dims)*t
    base=top-5-h
    text(ax,2,top,head,role,'m',ha='left',weight='bold')
    x=4
    for r,c in dims:
        tiles(ax,x,base,r,c,t,role)
        text(ax,x+c*t/2,base-2.6,str(r),role,'s')
        x+=c*t+g
    return base-5
dims12=[(d,12//d) for d in (1,2,3,4,6,12)]
b=row(12,74,'sujet',dims12,'12 : 6 diviseurs')
b=row(7,b-3,'autre',[(1,7),(7,1)],'7 : 2 diviseurs')
row(1,b-3,'varie',[(1,1)],'1 : 1 seul diviseur')
save(fig,'05-010')
