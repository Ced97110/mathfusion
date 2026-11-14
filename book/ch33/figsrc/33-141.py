import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(66)
f=lambda v: 10+(v+2)/4*66
text(ax,44,61,'quotient = produit ÷ longueurs','encre','m')
line(ax,[(f(-2),40),(f(2),40)],'fixe')
for v in (-2,-1,0,1,2):
    ax.plot([f(v)]*2,[39,41],color=COL['fixe'],lw=0.8); text(ax,f(v),36.2,f'{v}'.replace('-','−'),'fixe','s')
box(ax,f(-1),43,f(1)-f(-1),7,'sujet',label='cosinus possibles',size='s')
disc(ax,f(0.7071),40,1.3,'resultat'); disc(ax,f(1.5),40,1.3,'limite')
arrow(ax,(f(0.7071),38),(f(0.7071),27),'resultat')
box(ax,36,15,38,10,'resultat',label='arccos 0,7071 ≈ 45°',size='s')
text(ax,69.5,31,'1,5 : pas d’angle','limite','s')
save(fig,'33-141')
