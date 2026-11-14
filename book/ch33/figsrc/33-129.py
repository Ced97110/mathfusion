import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(54)
f=lambda v: 44+v/90*28
for y,role,fill,t,c,cr in [(40,'sujet',True,'arcsinus : bouts compris','sin 90° = 1 existe','resultat'),(16,'autre',False,'arctangente : bouts exclus',"tan 90° n’existe pas",'limite')]:
    line(ax,[(f(-90)+1.6,y),(f(90)-1.6,y)],role,1.4)
    for v in (-90,90): disc(ax,f(v),y,1.6,role,fill=fill,lw=1.2)
    for v in (-90,90): text(ax,f(v),y-4.5,f'{v}°'.replace('-','−'),role,'s')
    text(ax,44,y+8,t,role,'m')
    text(ax,44,y-9,c,cr,'m')
save(fig,'33-129')
