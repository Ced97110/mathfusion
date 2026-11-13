import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig,ax=canvas(56)
c=3.2; x0=7.2; y=22
for k in range(23):
    role='sujet' if k<20 else 'fixe'
    ax.add_patch(Rectangle((x0+k*c,y),c,5,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))
for g in range(4):
    ax.add_patch(Rectangle((x0+g*5*c,y),5*c,5,ec=COL['sujet'],fc='none',lw=1.3,zorder=3))
    text(ax,x0+(g*5+2.5)*c,31,str(g+1),'varie','m')
text(ax,44,46,'combien de fois 5 dans 23 ?','encre','l')
brace(ax,x0,x0+20*c,19,'resultat',label=r'$q=4$ tas de 5')
brace(ax,x0+20*c,x0+23*c,19,'fixe',label='reste 3')
save(fig,'05-029')
