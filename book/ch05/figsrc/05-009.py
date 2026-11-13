import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(50)
t=6
tiles(ax,16,14,3,4,t)
arrow(ax,(11,14),(11,32),'varie',both=True)
text(ax,6.5,23,'3 lignes','varie','s',rot=90)
brace(ax,16,40,32,'autre','4 colonnes',down=False)
box(ax,48,36,38,10,'sujet',label=r'$12 = 3 \times 4$')
box(ax,48,22,38,10,'resultat',label=r'$12 \div 3 = 4$')
box(ax,48,8,38,10,'resultat',label=r'$12 \div 4 = 3$')
arrow(ax,(41,30),(47,41),'sujet')
text(ax,28,7,'3 et 4 divisent 12','resultat','s')
save(fig,'05-009')
