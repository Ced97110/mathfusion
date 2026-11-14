import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
C=['sujet','varie']
for i,r1 in enumerate(C):
    for j,r2 in enumerate(C):
        x=22+j*15; y=27-i*15
        ax.add_patch(Rectangle((x,y),14,14,ec=COL['fixe'],fc=FILL['fixe'],lw=0.6,zorder=2))
        for dx,r in ((3.8,r1),(10.2,r2)):
            ax.add_patch(Circle((x+dx,y+7),2.6,ec=COL[r],fc=FILL[r],lw=0.7,zorder=3))
for i,r in enumerate(C): disc(ax,15,34-i*15,2.6,r)
for j,r in enumerate(C): disc(ax,29+j*15,47,2.6,r)
text(ax,15,26.5,'pion 1','encre','s')
text(ax,36,55,'pion 2','encre','s')
text(ax,36,6,'4 colorations','resultat','s')
text(ax,70,40,'2 × 2 = 4','resultat','l')
text(ax,70,28,'4 pions :','encre','s')
text(ax,70,19,'2×2×2×2','encre','m')
text(ax,70,11,'= 16','resultat','l')
save(fig,'49-306')
