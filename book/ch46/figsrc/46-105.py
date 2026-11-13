import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(85)
ex=[1,2,3,4,5]; pw=['2','4','8','16','32']
for i,(e,p) in enumerate(zip(ex,pw)):
    x=12+i*16
    disc(ax,x,62,4.2,'sujet',label=str(e),size='s'); disc(ax,x,28,4.2,'autre',label=p,size='s')
    arrow(ax,(x,57),(x,33),'resultat')
text(ax,4,76,r'exposant $n$','sujet','s',ha='left')
text(ax,4,17,r'puissance $2^n$','autre','s',ha='left')
text(ax,44,45,'','encre','s')
text(ax,44,6,'deux entiers, deux images','resultat','m')
save(fig,'46-105')
