import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,16,76,'ℤ/6ℤ','sujet','m'); text(ax,66,76,'ℤ/2ℤ × ℤ/3ℤ','autre','m')
P=['(0, 0)','(1, 1)','(0, 2)','(1, 0)','(0, 1)','(1, 2)']
for n,p in enumerate(P):
    y=60-n*11
    box(ax,6,y,20,8,'sujet',label=str(n),size='m')
    box(ax,52,y,28,8,'autre',label=p,size='m')
    arrow(ax,(26,y+4),(52,y+4),'varie')
save(fig,'52-172')
