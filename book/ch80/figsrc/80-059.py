import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
disc(ax,32,34,18,'sujet',fill=True); disc(ax,56,34,18,'autre',fill=True)
import numpy as np
a=np.linspace(-1,1,60); t=np.arccos(12/36*1.0)
# lens: intersection of the two discs
from matplotlib.patches import Circle
c1=Circle((32,34),18,transform=ax.transData); 
lens=Circle((56,34),18,fc=FILL['resultat'],ec=COL['resultat'],lw=1.4,zorder=3); ax.add_patch(lens); lens.set_clip_path(c1)
text(ax,24,34,r'$U$','sujet','l'); text(ax,64,34,r'$W$','autre','l')
text(ax,44,34,r'$U\cap W$','resultat','m')
text(ax,44,58,r'$U\wedge W=U\cap W$','encre','l')
text(ax,44,10,'vecteurs communs à U et à W','resultat','s')
save(fig,'80-059')
