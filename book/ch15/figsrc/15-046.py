import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,44,71,r'1 boîte $=x$','fixe','m')
w,g,gg=7,1,6
x=3.5
for n,lab in [(3,r'$3x$'),(4,r'$4x$'),(2,r'$2x$')]:
    x0=x
    for i in range(n): box(ax,x,50,w,8,'sujet',r=0.4); x+=w+g
    brace(ax,x0,x-g,59.5,'sujet',label=lab,down=False); x+=gg-g
for i in range(9): box(ax,8.5+8*i,12,7,8,'resultat',r=0.4)
brace(ax,8.5,8.5+8*9-1,11,'resultat',label=r'$9x$')
arrow(ax,(44,47),(44,24),'varie'); text(ax,66,36,r'$3+4+2=9$','varie','m')
save(fig,'15-046')
