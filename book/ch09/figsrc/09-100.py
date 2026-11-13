import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(56)
g=12; u=7
poly(ax,[(6,g),(6,g+5*u),(6+10/3*u,g)],'sujet')
poly(ax,[(44,g),(44,g+4.5*u),(44+3*u,g)],'autre')
a=math.degrees(math.atan(1.5))
for x in (6+10/3*u,44+3*u):
    ax.add_patch(Arc((x,g),10,10,theta1=180-a,theta2=180,color=COL['fixe'],lw=1.2,zorder=4))
text(ax,3.5,g+17,'5','sujet','s',ha='right'); text(ax,6+10/3*u/2,g-3.5,'10/3','sujet','s')
text(ax,41.5,g+15,'4,5','autre','s',ha='right'); text(ax,44+3*u/2,g-3.5,'3','autre','s')
text(ax,19,g+39,'rapport 1,5','sujet','s'); text(ax,60,g+35,'rapport 1,5','autre','s')
text(ax,34.5,g+7,'angle','fixe','s'); text(ax,76,g+7,'même angle','fixe','s')
save(fig,'09-100')
