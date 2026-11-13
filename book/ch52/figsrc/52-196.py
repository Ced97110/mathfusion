import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(70)
def tri(cx,vals,gs,role):
    P=[(cx,50),(cx-14,22),(cx+14,22)]
    for (i,j),g,pos in zip([(0,1),(0,2),(1,2)],gs,[(cx-15,38),(cx+15,38),(cx,17)]):
        a,b=P[i],P[j]; d=math.hypot(b[0]-a[0],b[1]-a[1]); u=((b[0]-a[0])/d,(b[1]-a[1])/d); line(ax,[(a[0]+u[0]*4.5,a[1]+u[1]*4.5),(b[0]-u[0]*4.5,b[1]-u[1]*4.5)],role,lw=1.0)
        text(ax,pos[0],pos[1],f'pgcd {g}',role,'s')
    for p,v in zip(P,vals): disc(ax,p[0],p[1],4.5,'sujet',label=str(v),size='m')
tri(22,[6,10,15],[2,3,5],'limite'); tri(66,[4,9,5],[1,1,1],'resultat')
text(ax,22,64,'pas deux à deux','limite','m'); text(ax,66,64,'deux à deux','resultat','m')
save(fig,'52-196')
