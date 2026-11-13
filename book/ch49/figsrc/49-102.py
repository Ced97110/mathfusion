import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,2,26,14,14,'sujet',label=r'$g$',size='l')
arrow(ax,(16,33),(40,33),'varie')
text(ax,28,37,r'$T$','varie','m')
xl,xr=52,80; ys={1:52,2:40,3:28,4:16}
for k,y in ys.items():
    disc(ax,xl,y,3.2,'fixe',label=str(k),size='s'); disc(ax,xr,y,3.2,'fixe',label=str(k),size='s')
for k in range(1,5):
    t=k%4+1
    arrow(ax,(xl+3.4,ys[k]),(xr-3.4,ys[t]),'sujet')
text(ax,xl,60,r'$x$','encre','m'); text(ax,xr,60,r'$gx$','encre','m')
text(ax,66,68,r'$T(g)$ : bijection de $S$','sujet','m',weight='bold')
save(fig,'49-102')
