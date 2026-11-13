import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def mini(x,y,s,orange):
    ax.add_patch(Rectangle((x,y),s,s,ec=COL['fixe'],fc=FILL['fixe'],lw=0.6,zorder=2))
    for k,(a,b) in enumerate(((.25,.75),(.75,.75),(.25,.25),(.75,.25))):
        c='varie' if k in orange else 'sujet'
        ax.add_patch(Circle((x+a*s,y+b*s),s*0.17,ec=COL[c],fc=FILL[c],lw=0.6,zorder=3))
box(ax,2,6,28,48,'sujet',fill=False)
text(ax,16,59,'4 rotations','sujet','s')
for k,t in enumerate(['0°','90°','180°','270°']):
    box(ax,6,11+k*10.5,20,8,'sujet',label=t,size='s')
box(ax,40,6,46,48,'autre',fill=False)
text(ax,63,59,'16 colorations','autre','s')
mini(44,30,10,(0,)); mini(72,30,10,(1,))
arrow(ax,(56,35),(70,35),'varie'); text(ax,63,40,'90°','varie','s')
text(ax,49,25,'avant','encre','s'); text(ax,77,25,'après','encre','s')
arrow(ax,(30.5,30),(38.5,30),'varie'); text(ax,34.5,34,'agit','varie','s')
save(fig,'49-012')
