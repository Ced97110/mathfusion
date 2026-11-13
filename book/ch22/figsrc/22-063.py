import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,46,r'$5\neq 7$','limite','l')
f=numberline(ax,8,80,10,0,8,arrow_right=False)
box(ax,f(0),13,f(5)-f(0),9,role='sujet',label=r'$\sqrt{16+9}=5$')
box(ax,f(0),26,f(4)-f(0),9,role='autre',label=r'$\sqrt{16}=4$'); box(ax,f(4),26,f(7)-f(4),9,role='autre',label=r'$\sqrt{9}=3$')
line(ax,[(f(7),26),(f(7),11)],'autre',dash=True)
save(fig,'22-063')
