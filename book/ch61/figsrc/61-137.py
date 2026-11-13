import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(76)
x0,x1=10,78; f=numberline(ax,x0,x1,44,-2,2,arrow_right=False,tick=1.2)
pts=[(f(-2+4*t/80),44+10*((-2+4*t/80)**2-2)) for t in range(81)]
line(ax,pts,'sujet',lw=1.1)
r=math.sqrt(2)
for s in (-1,1):
    ax.add_patch(Circle((f(s*r),44),1.6,ec=COL['limite'],fc=FILL['limite'],lw=1.0,zorder=4))
text(ax,f(-r)-2,52,r'$-\sqrt{2}$','limite','s'); text(ax,f(r)+2,52,r'$\sqrt{2}$','limite','s')
text(ax,44,70,r'$y=x^2-2$','sujet','s')
text(ax,44,8,'les deux zéros ne sont pas des fractions','limite','s')
save(fig,'61-137')
