import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,67,'120 = 5 × 4 × 3 × 2 × 1','encre','m')
def grid(x0,role):
    for i in range(10):
        for j in range(6): ax.add_patch(Rectangle((x0+i*3.2,34+j*3.2),3,3,ec=COL[role],fc=FILL[role],lw=0.3,zorder=2))
grid(9,'resultat'); grid(47,'fixe')
text(ax,25,58,r'pairs : 60 = $A_5$','resultat','m'); text(ax,63,58,'impairs : 60','fixe','m')
box(ax,4,8,30,9,'sujet',label=r'$q=4$ : 60',size='m'); box(ax,38,8,30,9,'sujet',label=r'$q=5$ : 60',size='m')
arrow(ax,(19,18),(19,33),'varie'); arrow(ax,(53,18),(34,33),'varie')
save(fig,'73-181')
