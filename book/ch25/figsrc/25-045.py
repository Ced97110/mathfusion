import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(58)
t=math.tan(math.radians(40)); A=(6,10)
poly(ax,[A,(50,10),(50,10+44*t)],'autre',fill=False)
poly(ax,[A,(26,10),(26,10+20*t)],'sujet')
ax.add_patch(Arc(A,16,16,theta1=0,theta2=40,color=COL['encre'],lw=0.9))
text(ax,21,13,'40°','encre','s')
text(ax,69,38,'Paris : 0,8391','sujet','s'); text(ax,69,30,'Lyon : 0,8391','autre','s')
text(ax,69,20,'même nombre','resultat','s'); text(ax,69,15,'« la » tangente de 40°','resultat','s')
text(ax,36,54,'même angle, deux tailles','encre','s')
save(fig,'25-045')
