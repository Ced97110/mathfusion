import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
x0,y0,c=18,22,6
for i in range(9):
    for j in range(4):
        ax.add_patch(Rectangle((x0+i*c,y0+j*c),c,c,ec=COL['sujet'],fc=FILL['sujet'],lw=0.5,zorder=2))
for bi in range(3):
    for bj in range(2):
        box(ax,x0+18*bi,y0+12*bj,18,12,'limite',fill=False,lw=1.4,r=0.3)
    brace(ax,x0+18*bi+0.5,x0+18*bi+17.5,y0+24+1,'resultat',label='3',down=False)
text(ax,44,68,r'$36=4\times 9$','sujet','l')
text(ax,44,59,'3 premier : divise le facteur 9','resultat','m')
text(ax,9,y0+12,'4\nlignes','sujet','s')
text(ax,44,15,r'6 divise 36 : 6 blocs de $2\times 3$','limite','m')
text(ax,44,7,'mais 6 ne divise ni 4 ni 9','limite','m')
save(fig,'05-118')
