import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def mini(x,y,s,orange):
    ax.add_patch(Rectangle((x,y),s,s,ec=COL['fixe'],fc=FILL['fixe'],lw=0.6,zorder=2))
    for k,(a,b) in enumerate(((.25,.75),(.75,.75),(.25,.25),(.75,.25))):
        c='varie' if k in orange else 'sujet'
        ax.add_patch(Circle((x+a*s,y+b*s),s*0.17,ec=COL[c],fc=FILL[c],lw=0.6,zorder=3))
box(ax,2,6,84,50,'fixe',fill=False,dash=True)
text(ax,44,61,'6 colorations à 2 pions orange','fixe','s')
adj=[(0,1),(1,3),(3,2),(2,0)]
for k,o in enumerate(adj): mini(8+k*20,36,10,o)
for k in range(3): arrow(ax,(19+k*20,41),(27+k*20,41),'varie')
text(ax,28,52,'un quart de tour','varie','s')
brace(ax,8,78,34,'sujet',label='orbite de 4')
mini(8,13,10,(0,3)); mini(28,13,10,(1,2))
arrow(ax,(19,18),(27,18),'varie',both=True)
brace(ax,8,38,11.5,'sujet',label='orbite de 2')
save(fig,'49-011')
