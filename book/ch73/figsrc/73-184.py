import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
for i in range(12):
    for j in range(10): ax.add_patch(Rectangle((4+i*2.1,10+j*2.1),1.9,1.9,ec=COL['fixe'],fc=FILL['fixe'],lw=0.3,zorder=2))
text(ax,17,5,r'$SL_2(F_5)$ : 120','fixe','s')
arrow(ax,(31,21),(50,21),'varie'); text(ax,40.5,25,'agit','varie','m')
import math
for k in range(6):
    a=math.radians(90+60*k); disc(ax,69+11*math.cos(a),24+11*math.sin(a),2.6,'sujet')
text(ax,69,5,'6 droites','sujet','m')
save(fig,'73-184')
