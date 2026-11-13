import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def mini(x,y,s,cols):
    ax.add_patch(Rectangle((x,y),s,s,ec=COL['fixe'],fc=FILL['fixe'],lw=0.6,zorder=2))
    for (a,b),c in zip(((.25,.75),(.75,.75),(.25,.25),(.75,.25)),cols):
        ax.add_patch(Circle((x+a*s,y+b*s),s*0.17,ec=COL[c],fc=FILL[c],lw=0.6,zorder=3))
for n in range(16):
    bits=[('varie' if (n>>b)&1 else 'sujet') for b in (3,2,1,0)]
    mini(40+(n%4)*11,8+(3-n//4)*11,9.5,bits)
text(ax,62,58,'16 colorations','resultat','m')
poly(ax,[(4,40),(20,40),(20,56),(4,56)],'fixe')
for x,y in ((6.5,53.5),(17.5,53.5),(6.5,42.5),(17.5,42.5)): disc(ax,x,y,2,'fixe',fill=False)
text(ax,12,35,'4 coins','fixe','s')
disc(ax,27,52,2.2,'sujet'); disc(ax,33,52,2.2,'varie')
text(ax,30,45,'2 choix','encre','s')
text(ax,20,24,'2 × 2 × 2 × 2','encre','l')
text(ax,20,15,'= 16','resultat','xl')
save(fig,'49-009')
