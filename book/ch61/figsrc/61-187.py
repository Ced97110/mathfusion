import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
items=[(r'$p/q$ irréductible, $p^3=2q^3$','sujet'),(r'$p^3$ pair, donc $p$ pair','varie'),(r'$p^3=8k$, donc $q^3=4k$','varie'),(r'donc $q$ est pair','varie'),(r'$p$ et $q$ pairs : contradiction','limite')]
ys=[70,55,40,25,10]
for (l,r),y in zip(items,ys): box(ax,4,y,60,10,r,label=l)
for i in range(4): arrow(ax,(34,ys[i]),(34,ys[i+1]+10),'fixe')
line(ax,[(67,27),(67,63)],'varie',lw=1.3)
text(ax,77,45,'étape','varie','s'); text(ax,77,41,'décisive','varie','s')
save(fig,'61-187')
