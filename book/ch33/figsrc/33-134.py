import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(66)
u=14; A=(16,30); B=(A[0]+4*u,30); C=(A[0]+2.625*u,30+1.453*u)
poly(ax,[A,B,C],'sujet')
text(ax,(A[0]+B[0])/2,26,'4','sujet','m')
text(ax,(A[0]+C[0])/2-3,(A[1]+C[1])/2+3,'3','sujet','m')
text(ax,(B[0]+C[0])/2+3,(B[1]+C[1])/2+3,'2','sujet','m')
a1=math.degrees(math.atan2(A[1]-C[1],A[0]-C[0])); a2=math.degrees(math.atan2(B[1]-C[1],B[0]-C[0]))+360*0
arc(ax,C,6,a1,a2+360 if a2<a1 else a2,'resultat',1.2)
text(ax,C[0],C[1]+4.5,'104,48°','resultat','m')
text(ax,70,50,'cos = −0,25','fixe','s')
f=lambda v: 12+v/180*64
line(ax,[(f(0),12),(f(180),12)],'fixe')
box(ax,f(0),14,64,6,'fixe',label='angles possibles d’un triangle',size='s')
disc(ax,f(104.48),12,1.3,'resultat')
text(ax,f(0),7,'0°','fixe','s'); text(ax,f(180),7,'180°','fixe','s'); text(ax,f(104.48),7,'104,48°','resultat','s')
save(fig,'33-134')
