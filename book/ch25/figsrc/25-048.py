import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(58)
A=(8,16); C=(48,16); B=(48,43)
poly(ax,[A,C,B],'fixe',fill=False); line(ax,[A,C],'sujet',lw=2.2); line(ax,[C,B],'varie',lw=2.2)
line(ax,[(C[0]-3,C[1]),(C[0]-3,C[1]+3),(C[0],C[1]+3)],'fixe')
ax.add_patch(Arc(A,18,18,theta1=0,theta2=34,color=COL['encre'],lw=1.0))
text(ax,4,17,'A','encre','s'); text(ax,51,46,'B','varie','s'); text(ax,51,13,'C','sujet','s')
text(ax,66,30,'a : opposé','varie','s'); text(ax,28,10,'b : adjacent','sujet','s')
text(ax,28,46,'gris : hors du rapport','fixe','s'); text(ax,68,10,'tan A = a/b','resultat','m')
save(fig,'25-048')
