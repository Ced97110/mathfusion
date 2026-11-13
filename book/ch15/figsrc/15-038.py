import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,44,80,r'$x=3$','fixe','l')
cols=[(23,'sujet',[r'$-x^2$',r'$3\times3=9$',r'$-9$'],'le carré, puis le signe'),(65,'autre',[r'$(-x)^2$',r'$(-3)\times(-3)$',r'$9$'],'le signe, puis le carré')]
for c,r,ls,cap in cols:
    for k,l in enumerate(ls): box(ax,c-19,60-21*k,38,11,r,label=l,size='l')
    for k in range(2): arrow(ax,(c,60-21*k),(c,49-21*k),r)
    text(ax,c,10,cap,r,'s')
text(ax,44,24,r'$\neq$','limite','xl')
save(fig,'15-038')
