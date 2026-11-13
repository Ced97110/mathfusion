import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(62)
x0,y0,L=10,46,66; h=L/12
poly(ax,[(x0,y0),(x0+L,y0),(x0+L,y0+h)],'sujet')
arc(ax,(x0,y0),16,0,4.76,'resultat',1.2)
text(ax,x0+34,y0+7,'4,76°','resultat','s')
text(ax,x0+L/2,y0-4,'12','sujet','s'); text(ax,x0+L+2,y0+h/2,'1','sujet','s',ha='left')
f=lambda v: 44+v/90*32
line(ax,[(f(-90),17),(f(90),17)],'fixe')
for v in (-90,0,90): ax.plot([f(v)]*2,[16,18],color=COL['fixe'],lw=0.8)
box(ax,f(-90),30,f(90)-f(-90),7,'autre',label='arctangente : −90° à 90°')
box(ax,f(0),22,f(90)-f(0),7,'sujet',label='triangle')
disc(ax,f(4.76),17,1.3,'resultat')
text(ax,f(-90),12.5,'−90°','fixe','s'); text(ax,f(90),12.5,'90°','fixe','s')
text(ax,f(4.76)-8,12.5,'4,76° est dedans','resultat','s')
save(fig,'33-131')
