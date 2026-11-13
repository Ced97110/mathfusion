import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
x0,x1=8,60; f=numberline(ax,x0,x1,14,-2,2,arrow_right=False,tick=1.2)
pts=[(f(-2+4*t/80),14+8*((-2+4*t/80)**2+1)) for t in range(81)]
line(ax,pts,'sujet',lw=1.1)
arrow(ax,(f(0),22),(f(0),15),'limite'); text(ax,f(0)+8,18,r'$\geq 1$','limite','s')
text(ax,34,64,r'$y=x^2+1$','sujet','s')
text(ax,34,6,'ℝ : jamais 0','limite','s') if False else None
box(ax,64,26,22,22,'autre')
text(ax,75,42,'ℂ','autre','s'); text(ax,75,34,r'$i$ et $-i$','autre','s')
arrow(ax,(64,37),(f(2)+2,37),'autre',curve=0.0) if False else None
save(fig,'61-138')
