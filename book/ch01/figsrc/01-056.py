import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,16,59,30,7,'fixe',label='0! : posé')
text(ax,52,62.5,'= 1','resultat','m',ha='left')
for y,l,r in zip([49,39,29,19],['1! = 1 × 0!','2! = 2 × 1!','3! = 3 × 2!','4! = 4 × 3!'],['= 1','= 2','= 6','= 24']):
    box(ax,16,y,30,7,'sujet',label=l)
    text(ax,52,y+3.5,r,'resultat','m',ha='left')
for y in [61,51,41,31]:
    arrow(ax,(60,y),(40,y-4.8),'varie',lw=0.9,curve=-0.4)
ax.add_patch(Rectangle((50.2,19),12.4,7,ec=COL['resultat'],fc='none',lw=1.2,zorder=3))
text(ax,44,10.5,'4 × 3 × 2 × 1 = 24','autre','m')
arrow(ax,(56.5,18.5),(56.5,12.5),'autre',both=True)
text(ax,44,4.5,'24 rangements de 4 livres','autre','s')
save(fig,'01-056')
