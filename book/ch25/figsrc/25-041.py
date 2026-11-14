import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(56)
L,Hh=28,28*math.tan(math.radians(40))
def tri(ax0,ay0):
    A=(ax0,ay0); C=(ax0+L,ay0); B=(ax0+L,ay0+Hh)
    poly(ax,[A,C,B],'fixe'); line(ax,[C,B],'varie',lw=2.0)
    return A,C,B
A,C,B=tri(4,14); ax.add_patch(Arc(A,18,18,theta1=0,theta2=40,color=COL['sujet'],lw=1.0))
A2,C2,B2=tri(48,14); ax.add_patch(Arc(B2,18,18,theta1=220,theta2=270,color=COL['sujet'],lw=1.0))
text(ax,39.5,26,'en face','varie','s'); text(ax,82,26,'touche','varie','s')
text(ax,18,8,'angle choisi : 40°','sujet','s'); text(ax,62,8,'angle choisi : 50°','sujet','s')
text(ax,44,48,'même côté, deux angles','encre','s')
save(fig,'25-041')
