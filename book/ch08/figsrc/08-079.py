import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
bw=9; g=1.5; x0=4
text(ax,x0,61,r'divisé par 3 : restes 0, 1, 2','encre','s',ha='left')
for i in range(3): box(ax,x0+i*(bw+g),48,bw,8,'sujet',label=str(i),size='s')
text(ax,x0,41,r'divisé par 7 : restes 0 à 6','encre','s',ha='left')
for i in range(7): box(ax,x0+i*(bw+g),28,bw,8,'sujet',label=str(i),size='s')
box(ax,x0,5,26,9,'limite',label=r'9 = 7 + 2',size='s')
arrow(ax,(x0+27,9.5),(x0+34,9.5),'varie')
text(ax,x0+36,9.5,'encore un paquet de 7','varie','s',ha='left')
save(fig,'08-079')
