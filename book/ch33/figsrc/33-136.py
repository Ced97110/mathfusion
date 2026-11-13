import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(60)
A=(8,34); L=58; h=L*0.2; B=(A[0]+L,34); C=(B[0],34+h)
poly(ax,[A,B,C],'sujet')
arc(ax,A,18,0,11.31,'resultat',1.2)
text(ax,34,46,'11,31°','resultat','s')
text(ax,A[0]+L/2,30,'100 m','sujet','m'); text(ax,B[0]+2,34+h/2,'20 m','sujet','m',ha='left')
box(ax,6,6,34,9,'sujet',label='20 ÷ 100 = 0,2')
arrow(ax,(41,10.5),(55,10.5),'varie'); text(ax,48,15,'arctan','varie','s')
box(ax,56,6,26,9,'resultat',label='11,31°')
save(fig,'33-136')
