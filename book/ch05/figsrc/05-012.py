import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(52)
for i in range(3):
    bx=4+i*11; box(ax,bx,34,9,9,'resultat')
    for a in (-2.5,0,2.5):
        for b in (-2.5,0,2.5): disc(ax,bx+4.5+a,38.5+b,0.9,'sujet')
text(ax,48,40,'3 divise 27','resultat','l',ha='left')
text(ax,48,35,'3 tas de 9, reste 0','resultat','s',ha='left')
for i in range(4):
    bx=4+i*8; box(ax,bx,10,6,9,'resultat')
    for b in (-2.2,2.2): disc(ax,bx+3,14.5+b,0.9,'sujet')
box(ax,37,10,6,9,'limite',dash=True)
for b in (-2.2,2.2): disc(ax,40,14.5+b,0.9,'limite')
text(ax,48,16,'4 ne divise pas 10','limite','l',ha='left')
text(ax,48,11,'4 parts de 2, reste 2','limite','s',ha='left')
save(fig,'05-012')
