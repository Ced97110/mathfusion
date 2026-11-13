import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
import math
def clock(cx,cy,n,mem,r=13):
    for k in range(n):
        t=math.radians(90-360/n*k); x,y=cx+r*math.cos(t),cy+r*math.sin(t)
        if k in mem:
            disc(ax,x,y,2,'sujet'); text(ax,cx+(r+5)*math.cos(t),cy+(r+5)*math.sin(t),str(k),'sujet','s')
        else: disc(ax,x,y,1.1,'fixe')
    ax.add_patch(Circle((cx,cy),r,fc='none',ec=COL['fixe'],lw=0.5,zorder=1))
clock(22,34,12,[0,3,6,9]); clock(66,34,6,[0,2,4])
text(ax,22,57,'horloge à 12 h','fixe','s'); text(ax,66,57,'horloge à 6 h','fixe','s')
text(ax,44,10,'H, N : une partie de G','sujet','s')
text(ax,44,4.5,'qui est elle-même un groupe','sujet','s')
save(fig,'47-045')
