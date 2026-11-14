import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
P=[(0,0),(1,1),(0,2),(1,0),(0,1),(1,2)]
text(ax,15,66,r'$\mathbb{Z}/2\times\mathbb{Z}/3$','sujet','m'); text(ax,66,66,r'$\cong\mathbb{Z}/6$','autre','m')
for i,p in enumerate(P):
    y=54-i*9
    box(ax,6,y,18,7,'sujet',label=rf'$({p[0]},{p[1]})$',size='s')
    disc(ax,66,y+3.5,3.6,'autre',label=str(i),size='s')
    arrow(ax,(26,y+3.5),(61.5,y+3.5),'resultat',both=True)
save(fig,'45-187')
