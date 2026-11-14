import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
f=numberline(ax,8,80,24,0,16,step=4,arrow_right=False)
for i in range(4):
    box(ax,f(2*i)+0.3,34,f(2)-f(0)-0.6,8,'sujet',label='2')
text(ax,62,38,r'$4x=8$','sujet','l')
box(ax,f(0),46,f(16)-f(0),8,'autre',label=r'$x^4=16$')
line(ax,[(f(8),26),(f(8),45)],'limite',dash=True)
text(ax,44,62,r'$x=2$ : $4x\neq x^4$','limite','l')
save(fig,'15-035')
