import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(62)
t=3.2
for c0,a,ok in [(3,3,True),(47,5,False)]:
    role='resultat' if ok else 'limite'
    box(ax,c0,44,9,8,role,label=str(a)); box(ax,c0+29,44,9,8,'sujet',label='12')
    arrow(ax,(c0+9.8,48),(c0+28.2,48),role)
    text(ax,c0+19,55,'diviseur de' if ok else 'pas diviseur de',role,'s')
    if ok:
        tiles(ax,c0+6,22,3,4,t)
        text(ax,c0+19,14,'3 rangées : plein',role,'s')
    else:
        tiles(ax,c0+10,22,5,2,t); tiles(ax,c0+10+2*t+2,22,2,1,t,'limite')
        text(ax,c0+19,14,'5 rangées : reste 2',role,'s')
save(fig,'05-011')
