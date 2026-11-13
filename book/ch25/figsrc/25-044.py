import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(66)
u=7; A=(6,22); C=(6+4*u,22); B=(6+4*u,22+3*u)
poly(ax,[A,C,B],'fixe',fill=False); line(ax,[A,C],'sujet',lw=2.0); line(ax,[C,B],'varie',lw=2.0)
ax.add_patch(Arc(A,12,12,theta1=0,theta2=37,color=COL['encre'],lw=1.0))
text(ax,20,17.5,'4','sujet','s'); text(ax,37.5,32.5,'3','varie','s'); text(ax,14,36,'5','fixe','s')
for y,r,t1,t2 in ((46,'resultat','opposé ÷ adjacent : tan','3 ÷ 4 = 0,75'),(28,'limite','adjacent ÷ opposé','4 ÷ 3 ≈ 1,333'),(10,'limite','opposé ÷ hypoténuse','3 ÷ 5 = 0,6')):
    box(ax,44,y,40,15,r); text(ax,64,y+10.5,t1,r,'s'); text(ax,64,y+4.5,t2,r,'m',weight='bold' if r=='resultat' else 'normal')
save(fig,'25-044')
