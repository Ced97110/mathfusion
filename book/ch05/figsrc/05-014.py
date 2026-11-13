import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(48)
t=5
tiles(ax,4,38,1,4,t); brace(ax,4,4+4*t,37.2,'sujet','1 rangée de 4')
text(ax,58,40.5,r'$4 \times 1 = 4$','resultat','l',ha='left')
tiles(ax,4,22,1,9,t); brace(ax,4,4+9*t,21.2,'sujet','1 rangée de 9')
text(ax,58,24.5,r'$9 \times 1 = 9$','resultat','l',ha='left')
box(ax,14,3,60,9,'resultat',label=r'$n \times 1 = n$ pour tout $n$')
save(fig,'05-014')
