import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,10,66,30,-1,4,labels=False)
for v in range(-1,5):
    text(ax,f(v),26.6,f'{v}'.replace('-','−'),'fixe','s')
for v in range(0,5): disc(ax,f(v),30,1.6,'sujet')
disc(ax,f(-1),30,1.6,'limite',fill=False)
box(ax,f(1)-6,48,12,9,'sujet',label=r'$x$'); arrow(ax,(f(1),48),(f(1),32.5),'varie')
box(ax,f(-1)-6,48,12,9,'autre',label=r'$x^{-1}$'); arrow(ax,(f(-1),48),(f(-1),32.5),'limite')
brace(ax,f(0),f(4),22,'fixe',label='monoïde : 0, 1, 2, 3…')
text(ax,44,8,r'$x^{-1}\mapsto -1$ : absent','limite','m')
save(fig,'49-054')
