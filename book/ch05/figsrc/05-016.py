import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(56)
text(ax,44,52,'se lit : 3 divise 27','encre','m')
box(ax,6,30,20,14,'sujet',label='3',size='xl')
box(ax,32,30,16,14,'varie',label=r'$\mid$',size='xl')
box(ax,54,30,28,14,'autre',label='27',size='xl')
text(ax,16,26,'diviseur','sujet','s'); text(ax,40,26,'divise','varie','s'); text(ax,68,26,'nombre divisé','autre','s')
box(ax,6,6,36,10,'resultat',label=r'$3 \mid 27$ : vrai')
box(ax,46,6,36,10,'limite',label=r'$27 \mid 3$ : faux')
text(ax,44,19.5,"l'ordre compte",'encre','s')
save(fig,'05-016')
