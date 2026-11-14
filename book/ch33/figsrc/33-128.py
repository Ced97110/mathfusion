import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(66)
X0,X1,Y0,Y1=14,80,12,54
fx=lambda x: X0+(math.log10(x)+1)/4*(X1-X0)
fy=lambda a: Y0+a/90*(Y1-Y0)
line(ax,[(X0,Y0),(X1+2,Y0)],'fixe'); line(ax,[(X0,Y0),(X0,Y1+3)],'fixe')
for v,s in [(1,'1'),(10,'10'),(100,'100'),(1000,'1 000')]:
    ax.plot([fx(v)]*2,[Y0-1,Y0+1],color=COL['fixe'],lw=0.8)
    text(ax,fx(v),Y0-3.5,s,'fixe','s')
text(ax,47,4,'pente','fixe','s')
for a in (0,45,90): text(ax,X0-5,fy(a),f'{a}°','fixe','s')
line(ax,[(X0,Y1),(X1,Y1)],'fixe',dash=True)
text(ax,47,Y1+5,'90° jamais atteint','encre','m')
xs=[10**(-1+4*i/120) for i in range(121)]
line(ax,[(fx(x),fy(math.degrees(math.atan(x)))) for x in xs],'sujet',1.5)
disc(ax,fx(1000),fy(89.94),1.2,'varie')
text(ax,X1-6,Y1-6,'89,94°','varie','s')
save(fig,'33-128')
