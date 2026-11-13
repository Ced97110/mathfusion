import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(52)
box(ax,22,40,44,10,'resultat',label=r'$12 = 3 \times 4$',size='l')
text(ax,22,31,'lu avec « diviseur »','sujet','s'); text(ax,66,31,'lu avec « multiple »','autre','s')
arrow(ax,(34,39.5),(24,33.5),'sujet'); arrow(ax,(54,39.5),(64,33.5),'autre')
for i,(a,b) in enumerate([(3,12),(4,12)]):
    box(ax,3,18-i*13,38,9,'sujet',label=f'{a} divise {b}')
    box(ax,47,18-i*13,38,9,'autre',label=f'{b} est multiple de {a}')
save(fig,'05-015')
