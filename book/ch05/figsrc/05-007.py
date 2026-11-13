import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(46)
t=2.6; x=18; y=28
text(ax,2,y+4,r'$n = 12$','sujet','m',ha='left')
for rows,cols in [(1,12),(2,6),(3,4)]:
    tiles(ax,x,y,rows,cols,t)
    brace(ax,x,x+cols*t,y-0.8,'sujet','12')
    x+=cols*t+5
text(ax,2,11.5,r'$n = 7$','autre','m',ha='left')
tiles(ax,18,10,1,7,t,'autre')
brace(ax,18,18+7*t,9.2,'autre','7')
text(ax,42,11.3,'une seule forme','autre','s',ha='left')
text(ax,66,40,'trois formes, même nombre','sujet','s')
save(fig,'05-007')
