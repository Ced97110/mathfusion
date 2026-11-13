import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(58)
f=numberline(ax,6,76,28,0,24,1,every=6,arrow_right=False)
for m in range(4,25,4):
    disc(ax,f(m),40,1.6,'resultat' if m==12 else 'sujet',fill=(m!=24))
    if m==24: disc(ax,f(m),40,1.6,'resultat',fill=False)
for m in range(6,25,6):
    disc(ax,f(m),16,1.6,'resultat' if m==12 else 'autre',fill=(m!=24))
    if m==24: disc(ax,f(m),16,1.6,'resultat',fill=False)
line(ax,[(f(12),38.2),(f(12),30)],'resultat',dash=True)
line(ax,[(f(12),21.5),(f(12),17.8)],'resultat',dash=True)
text(ax,2,47,'bus A : toutes les 4 min','sujet','s',ha='left')
text(ax,2,9,'bus B : toutes les 6 min','autre','s',ha='left')
text(ax,f(12),54,'premier passage commun','resultat','m')
arrow(ax,(f(12),52.3),(f(12),43),'resultat')
save(fig,'05-004')
