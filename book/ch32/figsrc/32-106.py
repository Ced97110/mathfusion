import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig,ax=canvas(56)
c,ox,oy=8,6,10
def cells(i0,j0,ni,nj,role):
    for i in range(ni):
        for j in range(nj):
            ax.add_patch(Rectangle((ox+(i0+i)*c,oy+(j0+j)*c),c,c,ec=COL[role],fc=FILL[role],lw=0.6,zorder=2))
cells(0,0,3,3,'sujet'); cells(3,0,1,3,'autre'); cells(0,3,3,1,'autre'); cells(3,3,1,1,'fixe')
text(ax,ox+12,oy+12,'u²','sujet','l'); text(ax,ox+28,oy+12,'u','autre','m'); text(ax,ox+12,oy+28,'u','autre','m'); text(ax,ox+28,oy+28,'1','fixe','m')
brace(ax,ox,ox+4*c,oy+4*c+0.5,'fixe','u + 1 = 4',down=False)
text(ax,68,50,'pour u = 3','fixe','s')
text(ax,66,43.5,'u² + 2u + 1','sujet','s'); box(ax,48,32,36,8,'sujet',label='9 + 6 + 1 = 16',size='s')
text(ax,66,27.5,'=','encre','m')
text(ax,66,23.5,'(u + 1)²','autre','s'); box(ax,48,12,36,8,'autre',label='(3 + 1)² = 16',size='s')
save(fig,'32-106')
