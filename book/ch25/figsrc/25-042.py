import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(60)
u=11; A=(16,14); C=(16+4*u,14); B=(16+4*u,14+3*u)
poly(ax,[A,C,B],'fixe',fill=False); line(ax,[A,C],'sujet',lw=2.2)
line(ax,[(C[0]-3,C[1]),(C[0]-3,C[1]+3),(C[0],C[1]+3)],'fixe')
ax.add_patch(Arc(A,16,16,theta1=0,theta2=37,color=COL['encre'],lw=1.0))
text(ax,38,8,'4 : adjacent','sujet','s'); text(ax,24,38,'5 : hypoténuse (touche)','fixe','s')
text(ax,74,30,'3 : ne touche pas','fixe','s'); text(ax,9,5,'angle choisi','encre','s')
arrow(ax,(10,8),(22.5,15.5),'encre')
save(fig,'25-042')
